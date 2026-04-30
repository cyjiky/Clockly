import { View, Pressable } from 'react-native';
import { Ionicons } from '@expo/vector-icons';
import { BlurView } from 'expo-blur';

export default function SearchButton() {
    return (
        <View className="flex-1 items-center justify-center">
            <Pressable 
                // onPress={() => console.log('Search button pressed!')}
                className="rounded-full overflow-hidden shadow-lg active:opacity-70"
            >
                <BlurView 
                    intensity={60}
                    tint="light"
                    className="w-16 h-16 items-center justify-center"
                >
                    <Ionicons name="search" size={28} color="black" />
                </BlurView>
            </Pressable>
        </View>
    );
}
