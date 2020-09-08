from ..repository import Repository
from ..repository.mongo import MongoRepository

class Service(object):
 def __init__(self,user_id, repo_client=Repository(adapter=MongoRepository)):
   self.repo_client = repo_client
   self.user_id = user_id
   self.sskudos = list()

   if not user_id:
     raise Exception("user id not provided")

 def find_all_kudos(self):
   return self.sskudos

 def find_kudo(self, repo_id):
   for kudo in self.sskudos:
       if kudo['id']==repo_id:
           return kudo
   return None

 def create_kudo_for(self, githubRepo):
   newkudo = {
      'id' : githubRepo['id'],
      'repo_name': githubRepo['name'],
      'full_name': githubRepo['full_name'],
      'description' : "Not available"
   }
   self.sskudos.append(newkudo)
   return newkudo

 def update_kudo_with(self, repo_id, githubRepo):
   records_affected = 0

   for kudo in self.sskudos:
       if kudo['id']==repo_id:
           kudo['repo_name'] = githubRepo['name']
           kudo['full_name'] = githubRepo['full_name']
           kudo['description'] = githubRepo['description']
           records_affected = 1
           # still need to update kudo is self.sskudos?
   return records_affected > 0

 def delete_kudo_for(self, repo_id):
   self.sskudos = [kudo for kudo in self.sskudos if kudo['id']!= repo_id]
   return origlen > len(self.sskudos)
