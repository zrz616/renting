<template>
    <div>
        <v-header></v-header>
        <v-content></v-content>

    </div>
</template>

<script>
    import header from '../components/header/index-header';
    import content from '../components/content/content';

    export default {
        components: {
            'v-header': header,
            'v-content': content
        }
    };
</script>

<style>
</style>
