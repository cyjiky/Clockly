import React from 'react';
import { View, Text, ScrollView } from 'react-native';
import MonthGrid from './MonthGrid';
import { MONTHS } from '@/constants/days';
import { MonthNavigationListProps } from '@/constants/props/calendarProps';

export default function MonthNavigation({
  year = new Date().getFullYear(),
  onDayPress,
}: MonthNavigationListProps) {
  const months = Array.from({ length: 12 }, (_, i) => i + 1);

  return (
    <ScrollView 
      className="flex-1 w-full bg-white"
      showsVerticalScrollIndicator={false}
      contentContainerStyle={{ paddingBottom: 24 }}
    >
      {months.map((month, index) => (
        <View key={`year-${year}-month-${month}`} className="mb-6">
          <View className="px-4 mb-2">
            <Text className="text-gray-800 text-lg font-bold capitalize">
              {MONTHS[index]} {year}
            </Text>
          </View>

          <MonthGrid 
            year={year} 
            month={month} 
            onDayPress={(day) => onDayPress?.(day, month, year)} 
          />
        </View>
      ))}
    </ScrollView>
  );
}