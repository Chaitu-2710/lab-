import 'package:flutter/material.dart';

void main() => runApp(const MyApp());

class MyApp extends StatelessWidget {
  const MyApp({super.key});
  @override
  Widget build(BuildContext context) => const MaterialApp(
        home: MyAnimatedWidget(),
      );
}

class MyAnimatedWidget extends StatefulWidget {
  const MyAnimatedWidget({super.key});
  @override
  State<MyAnimatedWidget> createState() => _MyAnimatedWidgetState();
}

class _MyAnimatedWidgetState extends State<MyAnimatedWidget>
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
      appBar: AppBar(title: const Text("Animation")),
      body: Center(
        child: FadeTransition(
          opacity: _controller,
          child: const Text("Hello Animation",
              style: TextStyle(fontSize: 26, fontWeight: FontWeight.bold)),
        ),
      ),
    );
  }
}