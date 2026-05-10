import React from 'react';
import { View, Text, TouchableOpacity } from 'react-native';
import { ChevronLeft, Search, Plus, AlignJustify } from 'lucide-react-native'; 
import type { CalendarScreenProps } from '@/constants/props/calendarProps';

const CalendarNavbar: React.FC<CalendarScreenProps> = ({
  onNavigateToEventCard, 
  onNavigateToChangeCard,
}) => {
  return (
    <View className="flex-row justify-between items-center px-4 w-full py-2 z-50">
      
      <TouchableOpacity 
        activeOpacity={0.7} 
        className="flex-row items-center bg-white rounded-full pl-2 pr-4 py-2.5 shadow-sm shadow-black/10"
      >
        <ChevronLeft color="#000" size={28} strokeWidth={2.5} />
        <Text className="text-black text-[19px] font-medium ml-0.5 tracking-tight">
          2026
        </Text>
      </TouchableOpacity>

      <View className="flex-row items-center bg-white rounded-full px-5 py-2.5 shadow-sm shadow-black/10 gap-6">
        
        <TouchableOpacity 
            activeOpacity={0.7}
            onPress={onNavigateToChangeCard}
            >
            <AlignJustify color="#000" size={24} strokeWidth={2.5} />
        </TouchableOpacity>

        <TouchableOpacity activeOpacity={0.7}>
            <Search color="#000" size={24} strokeWidth={2.5} />
        </TouchableOpacity>

        <TouchableOpacity 
            activeOpacity={0.7} 
            onPress={onNavigateToEventCard}
        >
            <Plus color="#000" size={28} strokeWidth={2.5} />
        </TouchableOpacity>
        
      </View>
    </View>
  );
};
export default CalendarNavbar;