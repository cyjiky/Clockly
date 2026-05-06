import React from 'react';
import { View, Text, TouchableOpacity } from 'react-native';
import { ChevronLeft, Search, Plus, AlignJustify } from 'lucide-react-native'; 
import type { CalendarNavbarProps } from '@/constants/props/calendarProps';

export default function CalendarNavbar({
  year = "2026",
//   onBackPress,
//   onViewTogglePress,
//   onSearchPress,
  onAddPress
}: CalendarNavbarProps) {
  return (
    <View className="flex-row justify-between items-center px-4 w-full py-2 z-50">
      
      <TouchableOpacity 
        activeOpacity={0.7} 
        // onPress={onBackPress}
        className="flex-row items-center bg-white rounded-full pl-2 pr-4 py-2.5 shadow-sm shadow-black/10"
      >
        <ChevronLeft color="#000" size={28} strokeWidth={2.5} />
        <Text className="text-black text-[19px] font-medium ml-0.5 tracking-tight">
          {year}
        </Text>
      </TouchableOpacity>

      <View className="flex-row items-center bg-white rounded-full px-5 py-2.5 shadow-sm shadow-black/10 gap-6">
        
        <TouchableOpacity 
            activeOpacity={0.7} 
            // onPress={onViewTogglePress}
        >
            <AlignJustify 
                color="#000" 
                size={24} 
                strokeWidth={2.5} 
            />
        </TouchableOpacity>

        <TouchableOpacity 
            activeOpacity={0.7} 
            // onPress={onSearchPress}
        >
            <Search 
                color="#000" 
                size={24} 
                strokeWidth={2.5} 
            />
        </TouchableOpacity>

        <TouchableOpacity 
            activeOpacity={0.7} 
            onPress={onAddPress}
        >
            <Plus 
                color="#000" 
                size={28} 
                strokeWidth={2.5} 
            />
        </TouchableOpacity>
        
      </View>

    </View>
  );
}