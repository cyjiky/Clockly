import { View, Text, Pressable } from 'react-native';
import { BlurView } from 'expo-blur';
import React, { useState } from 'react';

export default function TodayButton() {
    const [ isOpen, setIsOpen ] = useState(false);
    
    return (
        <View className="flex-1 items-center justify-center"> 
            
            <Pressable 
                // onPress={() => console.log('Today pressed!')}
                onPress={() => setIsOpen(true)}
                className="rounded-full overflow-hidden shadow-lg active:opacity-70 border border-white/70"
            >
                <BlurView 
                    intensity={60}
                    tint="light"
                    className="px-10 py-4 items-center justify-center"
                >
                    <Text className="text-black/80 text-sm font-extrabold tracking-widest text-center uppercase">
                        Today
                    </Text>
                </BlurView>
            </Pressable>
            
        </View>
    );
}
