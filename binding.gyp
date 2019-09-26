{
    "targets": [
        {
            "target_name": "hello",
            "sources": [ "hello.cc" ],
            "cflags!": [ "-fno-exceptions" ],
            "cflags_cc!": [ "-fno-exceptions" ],
            "include_dirs": [
                "<!@(node -p \"require('node-addon-api').include\")"
            ],
            "msvs_settings": {
                "VCCLCompilerTool": { "ExceptionHandling": 1 }
            }
        }
    ]
}
