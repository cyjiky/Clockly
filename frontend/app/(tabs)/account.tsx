import { View, Text } from 'react-native';
import WelcomeScreen from '@/components/cards/account/welcomeScreen';
// import RegisterScreen from '@/components/cards/account/registerCard'; -> TODO 

export default function AccountScreen() {
  return (
    <View className="flex-1 items-center justify-center bg-slate-100">
        {/* <Text className="text-black text-2xl font-extrabold tracking-widest text-center">
            Account Page!
        </Text> */}
        <WelcomeScreen />
        {/* <RegisterScreen /> */}
    </View>
  );
}