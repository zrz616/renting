<template>
    <div id="app">
        <v-header></v-header>
        <v-content></v-content>
        <v-footer></v-footer>
        <router-view></router-view>
    </div>
</template>

<script>
    import header from './components/header/header';
    import footer from './components/footer/footer';
    import content from './components/content/content';

    export default {
        components: {
            'v-header': header,
            'v-footer': footer,
            'v-content': content
        }
    };
</script>

<style>

</style>
