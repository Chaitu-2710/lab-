import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});
  @override
  Widget build(BuildContext context) => const MaterialApp(home: FadeAnim());
}

class FadeAnim extends StatefulWidget {
  const FadeAnim({super.key});
  @override
  State<FadeAnim> createState() => _FadeAnimState();
}

class _FadeAnimState extends State<FadeAnim>
    with SingleTickerProviderStateMixin {

  late final AnimationController _controller =
      AnimationController(vsync: this, duration: const Duration(seconds: 2))
        ..forward();

  @override
  void dispose() {
    _controller.dispose();
    super.dispose();
  }

  @override
  Widget build(BuildContext context) {
    return Scaffold(
      appBar: AppBar(title: const Text("Fade Animation")),
      body: Center(
        child: FadeTransition(
          opacity: _controller,
          child: Container(
            width: 200,
            height: 200,
            color: Colors.blue,
            alignment: Alignment.center,
            child: const Text("Fading In!",
                style: TextStyle(color: Colors.white, fontSize: 22)),
          ),
        ),
      ),
    );
  }
}