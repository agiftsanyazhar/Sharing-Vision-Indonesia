var editors = document.querySelectorAll(".quill-editor");

// Iterate over each element and initialize Quill
editors.forEach(function (editor) {
    new Quill(editor, {
        bounds: editor.parentElement.querySelector(".editor-container"),
        modules: {
            toolbar: [
                [{ font: [] }, { header: [1, 2, 3, 4, 5, 6, false] }],
                ["bold", "italic", "underline", "strike"],
                ["blockquote", "code-block"],
                [{ header: 1 }, { header: 2 }],
                [{ color: [] }, { background: [] }],
                [{ script: "super" }, { script: "sub" }],
                [
                    { list: "ordered" },
                    { list: "bullet" },
                    { indent: "-1" },
                    { indent: "+1" },
                ],
                ["link", "image", "video", "formula"],
                ["clean"],
            ],
        },
        theme: "snow",
    });
});
