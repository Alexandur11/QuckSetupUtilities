
class GrafanaLogging {
    let grafanaURL = None
    let serviceName = None
    let environment = None
    let grafanaUserID = None
    let grafanaLogAPIKey = None

    func sendLog(_ message: String) {
        let timestampNs = "\(Int(Date().timeIntervalSince1970 * 1_000_000_000))"

        let body: [String: Any] = [
            "streams": [[
                "stream": ["app": "None", "env": "None"],
                "values": [[timestampNs, message]],
            ]],
        ]

        let token = "\(grafanaUserID):\(grafanaLogAPIKey)"
        let base64 = Data(token.utf8).base64EncodedString()

        AF.request(
            grafanaURL,
            method: .post,
            parameters: body,
            encoding: JSONEncoding.default,
            headers: ["Content-Type": "application/json","Authorization": "Basic \(base64)"]
        )
        .response { response in
            // 204 No Content = success
            print(response.response?.statusCode ?? "no response")
        }
    }
}
