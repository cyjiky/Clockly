import { View, Pressable } from 'react-native';
import FontAwesome6 from '@expo/vector-icons/FontAwesome6';
import { BlurView } from 'expo-blur';

export default function TaskAddButton() {
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
                    <FontAwesome6 name="add" size={28} color="black" />
                </BlurView>
            </Pressable>
        </View>
    );
}
