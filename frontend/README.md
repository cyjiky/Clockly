# Welcome to frontend 👋

> Requiring Node.js >= 16.0

This is frontend side of the Clockly application

## Get started (manually)

1. Install dependencies

   ```bash
   npm install
   ```

2. Start the app

   ```bash
   npx expo start -c
   ```

   If you are testing on a physical device and experiencing connection issues, you can start Expo using a tunnel instead:

   ```bash
      npx expo start --tunnel
   ```

### Using Tunneling with Ngrok

Using an ngrok tunnel is the recommended approach when running the application inside a Docker container and testing it on a physical mobile device.

Follow these steps to configure and activate the tunnel:

1. Get an Ngrok Token
   - Sign up or log in at [ngrok.com](https://ngrok.com/)
   - Navigate to your dashboard and copy your unique Authtoken

2. Create a `.env` file in the root of the frontend directory (you can use `.env.example` as a template) and add your token:

```bash
EXPO_TOKEN=[ your_ngrok_token ]
```

3. Modify the `compose.yaml` file in the project root to ensure Docker uses the tunnel on startup. Update the frontend service command as follows:

```yaml
frontend:
  # ... other frontend configurations
  command: >
    sh -c "npm install -g @expo/ngrok && npx expo start --tunnel"
```

## Stucture

```text
📁.                                 project folder
 ├── 📁 backend                     server-side logic
 ├── 📁 frontend                    client-side application
 |    ├── 📁 app                    application routing & pages
 |    ├── 📁 assets                 static files
 |    ├── 📁 components             reusable UI elements
 |    |    ├── 📁 buttons           buttons components
 |    |    ├── 📁 cards             cards components
 |    |    └── 📁 navBar            navigation bar
 |    ├── 📁 constants              global constants & configurations
 |    |    └── 📁 props             component's props
 |    ├── 📁 hooks                  themes controllers
 |    ├── ⚙️ .env.example           environment variables example
 |    ├── 📝 package.json           dependencies & scripts
 |    ├── 🐳 Containerfile          container build
 |    └── 📍README.md               frontend description
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
