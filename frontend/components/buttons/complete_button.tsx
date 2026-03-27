import { useState } from 'react';
import { View, Pressable } from 'react-native';
import Entypo from '@expo/vector-icons/Entypo';
import { BlurView } from 'expo-blur';

export default function CompleteButton() {
    const [isCompleted, setIsCompleted] = useState(false);

    const handlePress = () => {
        setIsCompleted(!isCompleted);
        console.log(isCompleted ? 'Uncompleted!' : 'Completed!');
    };

    return (
        <View className="flex-1 items-center justify-center">
            
            <Pressable 
                onPress={handlePress}
                className="rounded-full overflow-hidden shadow-lg active:opacity-70"
            >
                <BlurView 
                    intensity={60}
                    tint="light"
                    className="w-16 h-16 items-center justify-center bg-white" 
                >
                    {isCompleted && (
                        <Entypo name="check" size={32} color="#1f2937" />
                    )}
                </BlurView>
            </Pressable>

        </View>
    );
    
}