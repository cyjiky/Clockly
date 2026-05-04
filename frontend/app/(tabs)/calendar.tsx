import { View, Text } from 'react-native';
import MonthNavigation from "components/MonthView/MonthNavigation"
import CalendarNavbar from '@/components/navBar/calendarNavBar';

export default function SearchButton() {
  return (
    <View className="flex-1 bg-slate-100">
      <CalendarNavbar />
        {/* <Text className="text-black text-2xl font-extrabold tracking-widest text-center">
            Search Button!
        </Text> */}
        
        <MonthNavigation />
    </View>
  );
}