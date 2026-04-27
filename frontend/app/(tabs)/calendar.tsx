import { View, Text } from 'react-native';
import MonthNavigation from '@/components/MonthView/monthNavigation';

export default function SearchButton() {
  return (
    <View className="flex-1 items-center justify-center bg-slate-100">
        <Text className="text-black text-2xl font-extrabold tracking-widest text-center">
            Search Button!
        </Text>
        
        <MonthNavigation />
    </View>
  );
}