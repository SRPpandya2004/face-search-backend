#for Backend run 

.\venv\Scripts\Activate.ps1

uvicorn app.main:app --port 8001   

deactivate  
----------------------------------------------------------------------------------------
#for Frontend Run

$env:Path += ";C:\Program Files\nodejs\"                           
>>                                                                                 
              
npm run dev
