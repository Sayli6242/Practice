const net = require("net")


const server = net.createServer(socket => {
    try {
        socket.write("hellow")
        socket.on("data", data => {
            console.log(data.toString())

        })
        socket.on("error", error => {
            console.log("this is error: ", error.toString())

        })
    } catch (error) {
        console.log(error)
    }

})
server.listen(8080)
