let iframeElements = document.getElementsByTagName("iframe");

for (let iframeElement of iframeElements) {
	if (iframeElements[0].getAttribute("title") === "Virtual Classroom") {
		let iframeSource = iframeElements[0].getAttribute("src");
		window.location.href = iframeSource;
		break;
	}
}
