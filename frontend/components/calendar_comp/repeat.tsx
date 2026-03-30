import { View, Text, Pressable } from 'react-native';
import * as React from 'react';
import { BlurView } from 'expo-blur';
import { DAYS } from '../../constants/days';

export default function RepeatComp() {
    const [selectedDays, setSelectedDays] = React.useState<string[]>([]);

    const toggleDay = (dayId: string) => {
        setSelectedDays((prevSelected) => {
            if (prevSelected.includes(dayId)) {
                return prevSelected.filter((id) => id !== dayId);
            }
            return [...prevSelected, dayId];
        });
    };

    return (
        <View className="flex-1 flex-row flex-wrap items-center justify-center gap-3 p-4">
            {DAYS.map((day) => {
                const isSelected = selectedDays.includes(day.id);

                return (
                    <Pressable 
                        key={day.id}
                        onPress={() => toggleDay(day.id)}
                        className={`rounded-full overflow-hidden shadow-lg active:opacity-70 ${
                            isSelected ? 'border-2 border-indigo-700' : 'border border-indigo-400'
                        }`}
                    >
                        <BlurView 
                            intensity={60}
                            className="w-10 h-10 items-center justify-center"
                        >
                            <Text 
                                className={`text-xl font-extrabold tracking-widest text-black`}
                            >
                                {day.label}
                            </Text>
                        </BlurView>
                    </Pressable>
                );
            })}
        </View>
    );
}