import { View, Text } from 'react-native';

export default function HomeScreen() {
  return (
    <View className="flex-1 items-center justify-center bg-slate-100">
      <View className="bg-indigo-600 px-8 py-6 rounded-3xl shadow-md border-2 border-indigo-300 gap-7">
        <Text className="text-white text-2xl font-extrabold tracking-widest text-center">
          Home Page!
        </Text>        
      </View>
    </View>
  );
}
