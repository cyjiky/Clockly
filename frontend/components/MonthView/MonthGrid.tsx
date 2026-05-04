import React from 'react';
import { View, Text, TouchableOpacity } from 'react-native';
import { MonthGridProps } from '@/constants/props/calendarProps';
import { DAYS_OF_WEEK } from '@/constants/days';

function MonthGrid({
  year = new Date().getFullYear(),
  month = new Date().getMonth() + 1,
  onDayPress,
}: MonthGridProps) {
  const getDaysInMonth = (y: number, m: number) => new Date(y, m, 0).getDate();
  
  const getFirstDayOfMonth = (y: number, m: number) => {
    const day = new Date(y, m - 1, 1).getDay();
    return (day + 6) % 7; 
  };

  const daysInMonth = getDaysInMonth(year, month);
  const firstDay = getFirstDayOfMonth(year, month);
  const gridCells: (number | null)[] = [];
  
  for (let i = 0; i < firstDay; i++) {
    gridCells.push(null);
  }
  
  for (let i = 1; i <= daysInMonth; i++) {
    gridCells.push(i);
  }

  return (
    // bg-white shadow-md
    <View className="w-full p-4 rounded-xl"> 
      <View className="flex-row mb-3">
        {DAYS_OF_WEEK.map((day, index) => (
          <View key={`header-${index}`} style={{ width: '14.28%' }} className="items-center justify-center">
            <Text className="text-gray-400 text-xs font-medium uppercase">
              {day}
            </Text>
          </View>
        ))}
      </View>

      <View className="flex-row flex-wrap">
        {gridCells.map((day, index) => (
          <View 
            key={`cell-${index}`} 
            style={{ width: '14.28%' }} 
            className="aspect-square p-1 items-center justify-center"
          >
            {day !== null && (
              <TouchableOpacity
                onPress={() => onDayPress?.(day)}
                activeOpacity={0.7}
                className="w-full h-full items-center justify-center"
              >
                <Text className="text-gray-800 text-base font-normal">
                  {day}
                </Text>
              </TouchableOpacity>
            )}
          </View>
        ))}
      </View>
    </View>
  );
}

export default MonthGrid;