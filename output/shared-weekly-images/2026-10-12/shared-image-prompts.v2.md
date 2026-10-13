# Linux week 2 image correction prompts

Final registration refinement: erase the full previous trait and replace it with two clean lines, `경로 지도로` / `파일을 수집·이동`, leaving at least 50 pixels of cream gap above progress. English: `Collects and moves files with path maps`, within the same trait area. Preserve progress panel position across languages.

Tool: built-in image_gen. Korean master first, English text-only edit.
Preserve original assets. Save accepted replacements as .v2.png and .en.v2.png.
Reviewed index.ko.md and index.en.md; preserve unrelated current title edits.

## thumbnail

Edit this cover keeping the exact 1734x907 wide canvas, title panel and all visible text '코딩 도감 #02', '두 번째 관찰, Linux', '경로와 파일', explorer identity and Path Forager orange-hood penguin identity. Replace outdoor backdrop with a very sparse Shell Cave fork: one simple flat brown rock arch at upper right, two dark cream/brown branching passages behind penguin, folder signpost at fork. Explorer with field guide left foreground, penguin map right foreground. Keep warm cream negative space across left title area and safe crop margins. Clean 16-bit pixel art, near-black outlines, burnt orange, restrained brown; no dense rock textures, gradients or dramatic lighting. Do not add text.

English replacements: {"코딩 도감 #02":"Codigdex #02","두 번째 관찰, Linux":"Linux · Observation 2","경로와 파일":"Paths and Files"}

## 02-absolute-relative-paths

Redesign middle diagram only as precise educational comparison following same square frame palette explorer/penguin identity. Title '절대 경로와 상대 경로'. One small line near top of comparison '현재 위치: /home/lupi/project'. Two equal columns. LEFT heading '절대 경로'; large address '/home/lupi/notes'; sequential route root folder '/' -> 'home' -> 'lupi' -> orange folder 'notes' (strict parent child chain). RIGHT heading '상대 경로'; large address '../notes'; clear route folder 'project' UP arrow labelled '..' to parent folder 'lupi', then down arrow to orange folder 'notes'; project and notes are SIBLINGS under lupi. No absolute address box in right column except shared current-location line at top. Both paths end at same notes folder. Small explorer and penguin bottom of middle, cream space. Bottom exact sentence '출발점은 달라도 같은 notes를 가리킨다'. Visible strings only those listed. No malformed Hangul, no extra decorative logos. 16-bit sparse warm cream black orange brown.

English replacements: {"절대 경로와 상대 경로":"Absolute and Relative Paths","현재 위치: /home/lupi/project":"Current directory: /home/lupi/project","절대 경로":"Absolute path","상대 경로":"Relative path","출발점은 달라도 같은 notes를 가리킨다":"Different starting points, same notes folder"}

## 03-file-commands-flow

Redesign as ONE dominant vertical four-stage file lifecycle flow on same square canvas. Preserve top frame, bottom takeaway panel, 16-bit clean cream black orange brown style and explorer identity. NO independent command tiles. Title '파일을 만들고 복사하고 옮기고 지우기'. Four spacious rows connected by clear downward arrows: 1 'mkdir notes' with new EMPTY folder notes. 2 'cp todo.txt notes/' show original todo.txt at left remains and second todo.txt inside notes at right; short caption '원본은 그대로'. 3 'mv notes/todo.txt project/today.txt' show notes now EMPTY at left and today.txt inside project at right, clear move arrow, short caption '원래 자리에는 없다'. 4 'rm project/today.txt' show project EMPTY and faded crossed-out today.txt outside it to indicate deletion, caption '휴지통 없이 삭제'. Original home todo.txt must remain unchanged by mv and rm, no implication it was deleted. Small explorer participates next to flow, no scenery or grass. Bottom '실행 전에 경로와 대상을 확인하자'. Render only specified strings and folder/file names notes project todo.txt today.txt. No find stage: this image explains four operation sequence, find discussed in prose.

English replacements: {"파일을 만들고 복사하고 옮기고 지우기":"Create, Copy, Move, Remove","원본은 그대로":"Original stays","원래 자리에는 없다":"Source is gone","휴지통 없이 삭제":"No trash can","실행 전에 경로와 대상을 확인하자":"Check the path and target first"}

## 04-path-forager-registration

Correct only right information area text spacing. Keep exact square frame layout left character portrait unchanged and all other non-text elements. Trait must be perfectly legible three lines '경로 지도를 따라' / '파일을 모으고' / '옮긴다' with clean Hangul no duplicated strokes or fragments. Shrink trait type moderately to keep final line at least 24px above progress panel. Keep stamp to right of trait. Leave progress bar in original Korean position, exactly five slots first TWO orange remaining THREE empty, '2/5'. All visible strings: '코딩 도감 등록', 'NO.007', '경로 채집가', '분류', '파일 탐색형', '특성', '경로 지도를 따라 파일을 모으고 옮긴다', '등록 완료', '2/5', 'NO.007 등록 완료'. Preserve character intrinsic hood map satchel exactly, no new props, blank cream portrait. No other text.

English replacements: {"코딩 도감 등록":"Codigdex Registration","경로 채집가":"Path Forager","분류":"Type","파일 탐색형":"File explorer","특성":"Trait","경로 지도를 따라 파일을 모으고 옮긴다":"Follows path maps to gather and move files","등록 완료":"Registered","NO.007 등록 완료":"NO.007 Registered"}
