import { View, Text } from 'react-native';
import MonthNavigation from "components/MonthView/MonthNavigation"
import CalendarNavbarNavigate from 'components/cards/calendar/calendarNavbarNavigate';

export default function CalendarScreen() {
  return (
    <View className="flex-1 bg-slate-100">
      <CalendarNavbarNavigate />
        
        <MonthNavigation />
    </View>
  );
}