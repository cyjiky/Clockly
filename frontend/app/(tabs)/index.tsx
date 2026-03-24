import { Image } from 'expo-image';
import { Platform, StyleSheet } from 'react-native';

import { HelloWave } from '@/components/hello-wave';
import ParallaxScrollView from '@/components/parallax-scroll-view';
import { ThemedText } from '@/components/themed-text';
import { ThemedView } from '@/components/themed-view';
import { Link } from 'expo-router';

export default function HomeScreen() {
  return (
    <ParallaxScrollView
      headerBackgroundColor={{ light: '#A1CEDC', dark: '#1D3D47' }}
      headerImage={
        <Image
          source={require('@/assets/images/partial-react-logo.png')}
          style={styles.reactLogo}
        />
      }>
      <ThemedView style={styles.titleContainer}>
        <ThemedText type="title">Welcome!</ThemedText>
        <HelloWave />
      </ThemedView>
      <ThemedView style={styles.stepContainer}>
        <ThemedText type="subtitle">Step 1: Try it</ThemedText>
        <ThemedText>
          Edit <ThemedText type="defaultSemiBold">app/(tabs)/index.tsx</ThemedText> to see changes.
          Press{' '}
          <ThemedText type="defaultSemiBold">
            {Platform.select({
              ios: 'cmd + d',
              android: 'cmd + m',
              web: 'F12',
            })}
          </ThemedText>{' '}
          to open developer tools.
        </ThemedText>
      </ThemedView>
      <ThemedView style={styles.stepContainer}>
        <Link href="/modal">
          <Link.Trigger>
            <ThemedText type="subtitle">Step 2: Explore</ThemedText>
          </Link.Trigger>
          <Link.Preview />
          <Link.Menu>
            <Link.MenuAction title="Action" icon="cube" onPress={() => alert('Action pressed')} />
            <Link.MenuAction
              title="Share"
              icon="square.and.arrow.up"
              onPress={() => alert('Share pressed')}
            />
            <Link.Menu title="More" icon="ellipsis">
              <Link.MenuAction
                title="Delete"
                icon="trash"
                destructive
                onPress={() => alert('Delete pressed')}
              />
            </Link.Menu>
          </Link.Menu>
        </Link>
        <ThemedText>
          {`Tap the Explore tab to learn more about what's included in this starter app.`}
        </ThemedText>
      </ThemedView>
      <ThemedView style={styles.stepContainer}>
        <ThemedText type="subtitle">Step 3: Get a fresh start</ThemedText>
        <ThemedText>
          {`When you're ready, run `}
          <ThemedText type="defaultSemiBold">npm run reset-project</ThemedText> to get a fresh{' '}
          <ThemedText type="defaultSemiBold">app</ThemedText> directory. This will move the current{' '}
          <ThemedText type="defaultSemiBold">app</ThemedText> to{' '}
          <ThemedText type="defaultSemiBold">app-example</ThemedText>.
        </ThemedText>
      </ThemedView>
    </ParallaxScrollView>
  );
}

const styles = StyleSheet.create({
  titleContainer: {
    flexDirection: 'row',
    alignItems: 'center',
    gap: 8,
  },
  stepContainer: {
    gap: 8,
    marginBottom: 8,
  },
  reactLogo: {
    height: 178,
    width: 290,
    bottom: 0,
    left: 0,
    position: 'absolute',
  },
});


// import React from 'react';
// import { View, Text, SafeAreaView, TouchableOpacity } from 'react-native';

// export default function TestTailwindScreen() {
//   return (
//     <SafeAreaView className="flex-1 bg-slate-100">
//       <View className="flex-1 items-center justify-center p-6">
        
//         {/* Карточка проверки */}
//         <View className="w-full bg-white p-8 rounded-3xl shadow-xl border border-slate-200">
          
//           <Text className="text-sm font-bold text-indigo-600 uppercase tracking-widest text-center mb-2">
//             Статус конфигурации
//           </Text>
          
//           <Text className="text-3xl font-black text-slate-900 text-center mb-4">
//             Tailwind <Text className="text-green-500">Активен</Text>
//           </Text>
          
//           <View className="h-1 w-full bg-slate-100 rounded-full mb-6" />

//           <Text className="text-slate-500 text-center leading-6 mb-8">
//             Если вы видите закругленные углы, тени и этот текст раскрашен — значит, 
//             <Text className="font-bold text-slate-700"> NativeWind v4 </Text> 
//             успешно подключен к вашему Expo проекту.
//           </Text>

//           {/* Интерактивная кнопка */}
//           <TouchableOpacity 
//             activeOpacity={0.7}
//             className="bg-indigo-600 py-4 rounded-2xl shadow-lg shadow-indigo-300"
//           >
//             <Text className="text-white text-center font-semibold text-lg">
//               Отлично, работаем дальше!
//             </Text>
//           </TouchableOpacity>

//         </View>

//       </View>
//     </SafeAreaView>
//   );
// }