module.exports = {
    devServer: {
        proxy: {
            "/api": {
                target: "http://localhost:80",
                ws: false,
                changeOrigin: true
            }
        }
    }
};