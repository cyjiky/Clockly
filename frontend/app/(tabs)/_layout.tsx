import { Tabs } from 'expo-router';
import React from 'react';

import FontAwesome from '@expo/vector-icons/FontAwesome';
import Ionicons from '@expo/vector-icons/Ionicons';
import MaterialCommunityIcons from '@expo/vector-icons/MaterialCommunityIcons';
import MaterialIcons from '@expo/vector-icons/MaterialIcons';

import { NativeTabs, Icon, Label } from 'expo-router/unstable-native-tabs';
import { Platform } from 'react-native';

export default function TabLayout() {

  if (Platform.OS === 'ios') {
    return (
      <NativeTabs>

      <NativeTabs.Trigger name="index">
        <Label>Home</Label>
        <Icon sf="house.fill" drawable="custom_android_drawable" />
      </NativeTabs.Trigger>

      <NativeTabs.Trigger name="calendar">
        <Label>Calendar</Label>
        <Icon sf="calendar" drawable="custom_android_drawable" />
      </NativeTabs.Trigger>

      <NativeTabs.Trigger name="tasks">
        <Label>Tasks</Label>
        <Icon sf="checkmark.circle" drawable="custom_android_drawable" />
      </NativeTabs.Trigger>

      <NativeTabs.Trigger name="account">
        <Label>Account</Label>
        <Icon sf="person.fill" drawable="custom_android_drawable" />
      </NativeTabs.Trigger>

    </NativeTabs>
    );
  }

  return (
    <Tabs>
      <Tabs.Screen
        name="index"
        options={{
          title: 'Home',
          tabBarIcon: ({ color }) => <FontAwesome size={28} name="home" color={color} />,
        }}
      />
      <Tabs.Screen
        name="calendar"
        options={{
          title: 'Calendar',
          tabBarIcon: ({ color }) => <Ionicons size={26} name="calendar" color={color} />,
        }}
      />
      <Tabs.Screen
        name="tasks"
        options={{
          title: 'Tasks',
          tabBarIcon: ({ color }) => <MaterialIcons size={28} name="task-alt" color={color} />,
        }}
      />
      <Tabs.Screen
        name="account"
        options={{
          title: 'Account',
          tabBarIcon: ({ color }) => <MaterialCommunityIcons size={28} name="account" color={color} />,
        }}
      />
    </Tabs>
  );
}