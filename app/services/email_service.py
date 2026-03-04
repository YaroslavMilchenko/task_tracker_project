import asyncio

async def send_welcome_email(email:str):
    print(f"\n[EMAIL SERVICE] Sending a letter to {email}...")
    
    await asyncio.sleep(3)
    
    print(f"\n[EMAIL SERVICE] Letter was successfully handed to {email}")