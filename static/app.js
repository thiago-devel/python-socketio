export default function createApp() {

    function initSocketIO(domain, port) {
        const socket = io.connect('//' + domain + ':' + port)

        return socket
    }

    return {
        initSocketIO,
    }
}