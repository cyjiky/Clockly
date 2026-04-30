import { View, Text } from 'react-native';
import AuthScreen from '@/components/cards/account/authScreen';

export default function AccountScreen() {
  return (
    <View className="flex-1 items-center justify-center bg-slate-100">
        {/* <Text className="text-black text-2xl font-extrabold tracking-widest text-center">
            Account Page!
        </Text> */}

        <AuthScreen/>

    </View>
  );
}