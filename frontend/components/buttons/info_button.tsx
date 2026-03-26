import { View, Pressable } from 'react-native';
import Feather from '@expo/vector-icons/Feather';
import { BlurView } from 'expo-blur';

export default function InfoButton() {
    return (
        <View className="flex-1 items-center justify-center">
            <Pressable 
                onPress={() => console.log('Today pressed!')}
                className="rounded-full overflow-hidden shadow-lg active:opacity-70"
            >
                <BlurView 
                    intensity={60}
                    tint="light"
                    className="w-16 h-16 items-center justify-center"
                >
                    <Feather name="info" size={28} color="black" />
                </BlurView>
            </Pressable>
        </View>
    );
}