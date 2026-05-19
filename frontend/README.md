# Welcome to frontend 👋
> Requiring Node.js >= 16.0

This is frontend side of the Clockly application

## Get started

1. Install dependencies

   ```bash
   npm install 
   ```

2. Start the app

   ```bash
   npx expo start -c

   <!-- or  -->

   npx expo start --tunnel

   ```

## Stucture

```text
📁.                                 project folder
 ├── 📁 backend                     server-side logic
 ├── 📁 frontend                    client-side application
 |    ├── 📁 app                    application routing & pages
 |    ├── 📁 assets                 static files
 |    ├── 📁 components             reusable UI elements
 |    ├── 📁 constants              global constants & configurations
 |    ├── 📁 hooks                  custom state & lifecycle hooks
 |    ├── 📝 package.json           dependencies & scripts
 |    ├── 📍README.md               frontend description
 |    └── 🐳 Containerfile          container build
 ├── 🐳 compose.yaml                docker compose orchestration
 ├── 📄LICENCE                      LICENCE
 └── 📝README.md                    project description
```


## Access the frontend

- Base URL: <http://127.0.0.1:8081>


In the output, you'll find options to open the app in a

- [development build](https://docs.expo.dev/develop/development-builds/introduction/)
- [Android emulator](https://docs.expo.dev/workflow/android-studio-emulator/)
- [iOS simulator](https://docs.expo.dev/workflow/ios-simulator/)
- [Expo Go](https://expo.dev/go), a limited sandbox for trying out app development with Expo

## Learn more

- [Expo documentation](https://docs.expo.dev/): Learn fundamentals, or go into advanced topics with our [guides](https://docs.expo.dev/guides).
