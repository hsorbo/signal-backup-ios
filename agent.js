Interceptor.attach(Module.getExportByName("SQLCipher", "sqlite3_prepare_v3"), {
    onEnter(args) {
        const sql = args[1].readUtf8String()
        const m = sql.match(/PRAGMA key = "x'(\w+)'"/);
        if (m !== null) {
            const key = m[1];
            send({ event: 'found-key', key });
        }
    }
});

Interceptor.attach(Module.getExportByName("SQLCipher", "sqlite3_open_v2"), {
    onEnter(args) {
        const filename = args[0].readUtf8String()
        send({ event: 'db-opened', filename });
    }
});