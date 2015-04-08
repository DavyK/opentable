tinymce.init({
        selector: "textarea",
		theme: "modern",
		    width: "800",
	        resize: "both",
            plugins: [
              "advlist", "autolink", "lists", "link", "image", "charmap", "preview", "hr", "anchor", "pagebreak",
              "searchreplace", "wordcount", "visualblocks", "visualchars", "code", "fullscreen",
              "insertdatetime", "media", "nonbreaking", "contextmenu", "directionality",
              "emoticons", "template", "paste", "textcolor", "colorpicker", "textpattern", "wordcount"
            ],


		    toolbar1: "undo redo | bold italic underline | alignleft aligncenter alignright alignjustify | bullist numlist outdent indent",
  		    toolbar2: "forecolor backcolor | emoticons | link",
            templates: [
               {title: 'Test template 1', content: 'Test 1'},
               {title: 'Test template 2', content: 'Test 2'}
            ]
		});

