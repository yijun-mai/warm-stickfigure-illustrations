# 单张提示词与编辑模板

## 生成

按具体任务填入下面字段，删掉无用项。可以中英混用；图上文案必须明确写成中文原文。

```text
Generate ONE standalone [aspect ratio; default 16:9] Chinese editorial doodle illustration.
Purpose: [article passage / concept / scene].
Core meaning: [one sentence].
Scene and action: [who is doing what, with whom, and what objects are essential].
Character: minimalist LINE stick figures, round slightly uneven unfilled heads, thin line torso and limbs, small dot eyes, expressive eyebrows and mouth. [specific readable emotion and matching pose]. Torso exactly ONE pen stroke, not a closed shirt outline; no detailed clothing, hairstyle, fingers or realistic anatomy. Not a solid-black blob or detailed cartoon body.
Style: warm friendly spontaneous hand-drawn notebook/whiteboard doodle. Flowing slightly wobbly pen lines with gentle line-weight variation; intentional natural imperfection, still clean and readable. No polished vector geometry.
Background: [clean cream / pale blue / pale green / peach / lavender / white]. Keep it bright and quiet.
Palette: [coordinated accents]. Clear contrast, playful and warm, no oversaturated clutter. Optional translucent highlighter [where it serves meaning].
Composition: [simple scene / comparison / relation / path / small comic]. Clear visual order, breathing room, no dense text page.
Exact on-image Chinese text: [quoted short labels, or "none"]. Rounded legible handwritten Chinese; lively heavier title only if requested. No extra invented text, numbers, signatures, watermarks or labels.
Doodle accents: [only the useful arrow / bubble / star / question mark / movement line / irregular frame].
Avoid: realistic people, photography, 3D, modelling, complex gradients, glossy shading, polished commercial vector illustration, rigid geometry, complex background, excess decoration, cold tech interface, emotionless standing figures.
```

不要照抄括号和字段名到图上。背景不强制白；不同时强制“空表情”和“情绪鲜明”。没有需要的装饰字段可删。数据和对话不得因配图方便而编造。

## 连续图补充

```text
Keep the same stick-figure proportions, pen style, facial language and accent-color family as the accepted reference. Reference image is STYLE/CHARACTER reference, not a request to duplicate its scene. New scene: [...]. Change the action to [...].
```

每张独立出图，记录实际提示词。若工具只能接有限参考图，使用最少必要参考，不能假装看过缺失图片。

## 局部编辑

```text
Edit the supplied image. Change ONLY [target and desired change]. Preserve [characters not targeted, composition, line style, colors, aspect ratio, existing text and other objects]. Match the existing hand-drawn lines and background. Do not add new labels or extra decoration.
```

删除文字时补回原有背景；错字少则局部修复，错字多可缩短标注后重生成。透明背景请求必须保留真正透明度，不用白底冒充透明。
