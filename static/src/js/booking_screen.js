/** @odoo-module **/

import { Component, useState, onMounted } from "@odoo/owl";
import { useService } from "@web/core/utils/hooks";
import { registry } from "@web/core/registry";

export class TransportBookingScreen extends Component {
    static template = "transport.booking.screen";

    setup() {
        this.orm = useService("orm");
        this.state = useState({
            routes: [],
            vehicles: [],
            route_id: null,
            vehicle_id: null,
            seats: 1,
            amount: 0.0,
            customer_name: "",
            booking_date: this._today(),
            feedback: null,
        });

        onMounted(async () => {
            await this._loadData();
        });
    }

    async _loadData() {
        try {
            // Explicitly calls updated backend methods that query Fleet
            const [routes, vehicles] = await Promise.all([
                this.orm.call("transport.booking", "get_routes_data", []),
                this.orm.call("transport.booking", "get_vehicles_data", [])
            ]);
            this.state.routes = routes || [];
            this.state.vehicles = vehicles || [];
        } catch (e) {
            console.error("Failed to load reference data:", e);
            this._showFeedback("Failed to load Fleet records. Check server.", "danger");
        }
    }

    _today() {
        return new Date().toISOString().split('T')[0];
    }

    onRouteChange(ev) {
        this.state.route_id = ev.target.value ? parseInt(ev.target.value) : null;
    }

    onVehicleChange(ev) {
        this.state.vehicle_id = ev.target.value ? parseInt(ev.target.value) : null;
    }

    get canConfirm() {
        const s = this.state;
        return s.route_id && s.vehicle_id && s.customer_name.trim() !== "";
    }

    async onConfirm() {
        if (!this.canConfirm) return;
        try {
            const result = await this.orm.call(
                "transport.booking",
                "create_booking",
                [],
                { data: { ...this.state } }
            );
            if (result.success) {
                this._showFeedback(`✅ Booking #${result.id} saved!`);
                this.state.customer_name = "";
            }
        } catch (error) {
            this._showFeedback("Booking failed.", "danger");
        }
    }

    _showFeedback(message, type = "success") {
        this.state.feedback = { message, type };
        setTimeout(() => { this.state.feedback = null; }, 3000);
    }
}

registry.category("actions").add("transport.booking.screen", TransportBookingScreen);