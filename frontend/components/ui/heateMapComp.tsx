import React, { useMemo } from 'react';
import { View, ScrollView } from 'react-native';

export default function HeatMapComp() {
  const activityData: number[][] = useMemo(() => {
    return Array.from({ length: 52 }).map(() =>
      Array.from({ length: 7 }).map(() => Math.floor(Math.random() * 5)) 
    );
  }, []);

  const getColorClass = (level: number): string => {
    switch (level) {
      case 1: return 'bg-white/40';
      case 2: return 'bg-white/60';
      case 3: return 'bg-white/80';
      case 4: return 'bg-white';
      default: return 'bg-indigo-800/50'; 
    }
  };

  return (
    <ScrollView 
      horizontal 
      showsHorizontalScrollIndicator={false}
      className="my-4" 
    >
      <View className=" px-2 py-2 rounded-md shadow-md border-1 border-indigo-300 flex-row gap-1">
        
        {activityData.map((week: number[], weekIndex: number) => (
          <View key={`week-${weekIndex}`} className="flex-col gap-1">
            
            {week.map((dayLevel: number, dayIndex: number) => (
              <View
                key={`day-${weekIndex}-${dayIndex}`}
                className={`w-3 h-3 rounded-sm ${getColorClass(dayLevel)}`}
              />
            ))}
            
          </View>
        ))}

      </View>
    </ScrollView>
  );
}