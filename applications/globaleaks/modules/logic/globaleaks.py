import randomizer
from db import db

class Globaleaks(object):

    def __init__(self):
        self._db = db
        
    def create_target(self, name, category, desc, url, type, info):
        target_id = self._db.target.insert(name=name, 
            category=category,
            desc = desc, url=url, type=type, info=info,
            status="subscribed" #, last_send_tulip=None,
            #last_access=None, last_download=None,
            #tulip_counter=None, download_counter=None
           )
        self._db.commit()
        return target_id
        
    def delete_target (self, id):
       self._db(self._db.target.id==id).delete()
       pass

    def get_targets(self, target_set):
        if target_set == "ANY":
            return self._db(self._db.target).select()
        return self._db(self._db.target.category==target_set).select()
        
    def get_target(self, target_id):
        return self._db(self._db.target.id==target_id).select().first()
        
    def create_leak(self, title, desc, leaker, material, target_set, tags="", number=None):
        #FIXME insert new tags into DB first
        
        #Create leak and insert into DB
        leak_id = self._db.leak.insert(title = title, desc = desc,
            submission_timestamp = time.time(),
            leaker_id = 0, spooled=False)
        
        targets = gl.get_targets(target_set)
        
        for t in targets:
        #Create a tulip for each target and insert into DB
        #for target_url, allowed_downloads in targets.iteritems():
            self._db.tulip.insert(url = randomizer.generate_tulip_url(),
                leak_id = leak_id,
                target_id = t.id, #FIXME get target_id_properly
                allowed_accesses = 0, # inf
                accesses_counter = 0,
                allowed_downloads = 5,
                downloads_counter = 0,
                expiry_time = 0)
        
        self._db.tulip.insert(url = number,
                leak_id = leak_id,
                target_id = 0, #FIXME get target_id_properly
                allowed_accesses = 0, # inf
                accesses_counter = 0,
                allowed_downloads = 5,
                downloads_counter = 0,
                expiry_time = 0)
        
        self._db.commit()
        return leak_id
        
    def get_leaks(self):
        pass
        
    def get_leak(self, leak_id):
        pass
        
    def get_tulips(self, leak_id):
        pass
        
    def get_tulip(self, tulip_id):
        pass
