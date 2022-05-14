# Messaging App (To Be Named)

### Start Development Server
Requirements:
1. Python v3.10+
2. VirtualEnv
    1. `python3 -m pip install virtualenv`
    2. `cd server`
    3. `python3 -m virtualenv venv`

Steps:
1. `cd server`
2. `source venv/scripts/activate`
3. `python3 -m pip install -r requirements.txt`
4. `uvicorn main:app --reload`
5. Visit `localhost:8000/status`

### Start Development App
Requirements:
1. npm v8+
2. Expo Go Mobile App
3. Expo CLI
    1. `npm install --global expo-cli`

Steps:
1. `cd app`
2. `npm install`
3. `expo start`
