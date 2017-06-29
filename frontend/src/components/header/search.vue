<template>
    <div class="ui vertical basic segment seachpanel">
        <div class="ui container searchpanel">
            <div class="ui borderless menu in-searchpanel">
                <!-- searchbox -->

                <div class="ui input in-searchpanel" >
<!--                     <div class="ui form" >
                        <div class="field">
                            <select style="height: 63px;-moz-appearance: none;-webkit-appearance: none;">
                                <option value="2">清华大学</option>
                                <option value="1">北京大学</option>
                                <option value="0">北京五道口男子篮球学院</option>
                            </select>
                        </div>
                    </div> -->
                    <input v-model="school" type="text" placeholder="Search...">
                    <!--<input type="hidden" name="school">-->
                    <!--<i class="dropdown icon in-dropdown-searchpanel">-->
                        <!--<img class="image-dropdown in-dropdown-searchpanel" src="/static/image/租房项目切图/1首页/triangle_icon.png" alt="" />-->
                    <!--</i>-->
                    <!--<div class="default text in-dropdown-searchpanel">-->
                        <!--想去哪个学校附近租房？选择学校名字-->
                    <!--</div>-->
                    <!--<div class="menu">-->
                        <!--<div class="item" data-value="1">清华大学</div>-->
                        <!--<div class="item" data-value="2">北京大学</div>-->
                        <!--<div class="item" data-value="3">更多...</div>-->
                    <!--</div>-->
                </div>
                <!-- searchbutton -->
                <div @click="submit" class="ui button in-searchpanel">
                    搜索
                </div>
            </div>
        </div>
    </div>
</template>

<script>
    export default {
        data () {
            return {
                school: ''
            };
        },
        methods: {
            submit () {
                this.$router.push({name: 'list', params: {'school_name': this.school}});
            }
        }
    };
</script>

<style>
    /*--------------------------------searchpanel--------------------------------*/
    .ui.vertical.basic.segment.seachpanel {
        height: 109px;
        background-color: rgba(252, 195, 22, 0.8);
        /*note1: the opacity has been set 0.8 as in above*/
        /*note2: below opacity: 0.6 will be also inherited by the son blocks*/
        /*opacity: 0.6;*/
        /*note: see note in son container*/
        /*padding: 0;*/
        padding-top: 23px;
        padding-bottom: 23px;
        position: relative;
        top: 506px;
        /*doubt: if a translate is used, then a left is needed.
        because the positioning point, no matter translated or not
        is put at the same place as its father's positioning point.*/
        /*transform: translate(-50%,0);*/
    }

    .ui.container.searchpanel,
    .ui.borderless.menu.in-searchpanel {
        width: 577px;
        height: 63px;
        /*note: for removing the white borders*/
        border: 0;
        border-radius: 0 10px 10px 0;
        /*note: it is better to margin a container by padding in its father box*/
        padding: 0;
        margin: 0;
    }

    .ui.input.in-searchpanel {
        width: 458px;
        height: 63px;
        background-color: #ffffff;
        border: 0;
        border-radius: 0;
        padding: 0;
        margin: 0;
    }

    .dropdown.icon.in-dropdown-searchpanel {
        color: #ffffff;
    }

    .default.text.in-dropdown-searchpanel {
        /*min-width: 340px;*/
        font-size: 20px;
        /*or the font color will be overrided by .ui.dropdown > .default.text*/
        color: #979797 !important;
        padding: 24px 37px 25px 24px;
        margin: 0;
    }

    .image-dropdown.in-dropdown-searchpanel {
        margin: 29px 8px 24px auto;
    }

    .ui.button.in-searchpanel {
        width: 119px;
        height: 63px;
        border-radius: 0 8px 8px 0;
        background-color: #8dc63f;
        /*style for text in button*/
        padding-top: 19px;
        margin: 0 0 0 0;
        font-size: 20px;
        font-weight: bold;
        color: #ffffff;
    }
</style>
