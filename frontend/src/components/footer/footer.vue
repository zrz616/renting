<template>
    <div class="ui vertical segment footer">
        <div class="ui container footer">
            <div class="ui grid footer">
                <!-- firt column -->
                <div class="four wide column in-footer">
                    <div class="ui vertical text menu in-footer">
                        <div class="item header-in-menu-footer">
                            <h3 class="ui header">关于我们</h3>
                        </div>
                        <div class="item in-menu-footer">常见问题</div>
                        <div class="item in-menu-footer">联系我们</div>
                        <div class="item in-menu-footer">加入我们</div>
                    </div>
                </div>
                <!-- second column -->
                <div class="four wide column in-footer" style="padding-left: 31px;">
                    <div class="ui vertical text menu in-footer">
                        <div class="item header-in-menu-footer">
                            <h3 class="ui header">热门房源</h3>
                        </div>
                        <div class="item in-menu-footer">北京大学</div>
                        <div class="item in-menu-footer">清华大学</div>
                        <div class="item in-menu-footer">人民大学</div>
                        <div class="item in-menu-footer">北京邮电</div>
                    </div>
                </div>
                <!-- third column -->
                <div class="four wide column in-footer" style="padding-left: 62px;">
                    <div class="ui vertical text menu in-footer">
                        <div class="item header-in-menu-footer">
                            <h3 class="ui header">关注我们</h3>
                        </div>
                        <div class="item in-menu-footer">关注微信</div>
                        <div class="item in-menu-footer">关注微薄</div>
                        <div class="item in-menu-footer">关注头条号</div>
                        <div class="item in-menu-footer">关注知乎</div>
                    </div>
                </div>
                <!-- fourth column -->
                <div class="four wide column in-footer" style="padding-left: 93px;">
                    <div class="ui vertical text menu in-footer">
                        <div class="item header-in-menu-footer">
                            <h3 class="ui header">反馈问题</h3>
                        </div>
                        <div class="item in-menu-footer" style="line-height: 150%;">
                            欢迎写邮件向我们反馈<br />
                            邮箱地址：<br />
                            hi@mugglecoding.com
                        </div>
                    </div>
                </div>
            </div>
            <div class="ui divider in-footer"></div>
            <div class="text-left in-footer">
                Developed by Mugglecoding team catcuts
            </div>
            <div class="text-right in-footer">
                京ICP备15047012号-2
            </div>
        </div>
    </div>
</template>

<script>
</script>

<style>
    /*do not repeat yourself*/
    .ui.vertical.segment.footer {
        height: 281px;
    }

    .ui.container.footer {
        width: 879px;
        min-width: 879px;
        /*note: height is uncessary for a container*/
        /*height: 281px;*/
        /*note: better to use padding for a container than margin*/
    }

    .ui.grid.footer {

    }

    .four.wide.column.in-footer {
        padding-top: 24px;
        background-color: #ffffff;
    }

    .ui.vertical.text.menu.in-footer {

    }

    .item.header-in-menu-footer {
        min-width: 64px;
        font-size: 16px;
        color: #666666;
        padding-left: 0 !important;
        padding-bottom: 0 !important;
        margin-bottom: 20px !important;
    }

    .item.in-menu-footer {
        min-width: 48px;
        font-size: 12px;
        color: #979797;
        padding-left: 0 !important;
        margin-top: 0px !important;
        margin-bottom: 11px !important;
    }

    .ui.divider.in-footer {
        border: solid 1px #d8d8d8;
        margin-top: 19px;
    }

    .text-left.in-footer {
        min-width: 226px;
        font-size: 13px;
        color: #979797;
        margin-top: 8px;
        margin-bottom: 22px;
        display: inline-block;
    }

    .text-right.in-footer {
        min-width: 128px;
        font-size: 13px;
        color: #979797;
        margin-top: 8px;
        margin-bottom: 22px;
        margin-left: 508px;
        display: inline-block;
    }
</style>
