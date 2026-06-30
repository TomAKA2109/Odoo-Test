/** @odoo-module **/

import { patch } from "@web/core/utils/patch";
import { ListController } from "@web/views/list/list_controller";
import { onWillStart } from "@odoo/owl";

patch(ListController.prototype, {
    setup() {
        super.setup();
        onWillStart(async () => {
            if (this.props.resModel === "hr.simple.employee") {
                this.__hideCreateButton = true;
            }
        });
    },

    get canCreate() {
        if (this.__hideCreateButton) return false;
        return super.canCreate;
    }
});