<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0801.txt",
      "sha256": "21280d9a0946be399802afa4450de861b2ebb47507b96c7394b498261e87b81a",
      "bytes": 12769
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "35bfc7fa636c2c29147def687e52e81c026b4ccd44241a2d816fa63430ea36a8",
      "bytes": 1958
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "8c9dc8070fa756b845bf81e2219201805fa9702c6b54e02735af9a47785da09b",
      "bytes": 224512
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "833c998832eba7e8d7e03352eb9ce194cb1a09124284f04c882b47c4a5a5b611",
      "bytes": 553
    },
    {
      "path": "characters/Felix.md",
      "sha256": "1985fcd32417e4b85bfa07c6059dab48d28678f448f5fa85bf3b8f39a71b8779",
      "bytes": 531
    },
    {
      "path": "characters/Heo Jun.md",
      "sha256": "c8129079822b744210642d62701617165af597aea49f13d1daad76f1e356ec2f",
      "bytes": 716
    },
    {
      "path": "characters/The Prophet.md",
      "sha256": "8d927fa63a75f445066e83c55d0320bb504adc6cc346dcc46eddfd0a83b2e162",
      "bytes": 707
    },
    {
      "path": "characters/Yamamoto.md",
      "sha256": "e5c013c2ee8c01a1d68a33d806ab4eedb734db3f91de6dbc59b50a173da2fa24",
      "bytes": 574
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "8f35dc58e43912ac49e8f00d38d106f1430d346d27f8a4c09f50a87eb53641ab",
      "bytes": 247115
    }
  ],
  "estimated_tokens": 8833
}
-->

# Durable State Update — Chapter 801

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 801. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 801. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that
are absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
Before returning JSON, verify every `speaker` and `addressee` value contains at
least one Hangul character; use the Korean source spelling even when the same
person's English name appears in the reading copy. If no valid new pair exists,
return `"address_pairs": []`.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 801,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 801,
    "continuity_sources": [801],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "진태경",
      "addressee": "문경",
      "kinship": "kinship or role relation",
      "normal_address": "established English address",
      "speech_level": "speech level",
      "notes": "brief note"
    }
  ],
  "profile_updates": [
    {
      "path": "characters/Listed Profile.md",
      "current": "- **Role:** exact current full line",
      "replacement": "- **Role:** finished replacement full line"
    }
  ],
  "profile_creations": [
    {
      "filename": "English Name.md",
      "korean": "source name",
      "english": "English Name",
      "aliases": [],
      "role": "stable role",
      "personality": "stable traits",
      "voice": "stable voice",
      "relationships": "stable relationships"
    }
  ]
}

Use empty arrays when no name, address-pair, or profile change is required.
`profile_creations` is only for characters with no existing `characters/` file.
If the person already appears under Listed compact profiles, use `profile_updates`.

## Prior durable context

```json
{
  "active_continuity": [
    "Jin Taekyung is the World Hunter Federation’s Alliance Leader and is pursuing Main Quest [Cataclysm], which requires him to eliminate The Prophet within an unspecified time limit.",
    "The Prophet stopped all ten J1 transport vehicles and absorbed blood and a pale mist from the dead; the nature of this power is unknown.",
    "The Prophet left a message intended to lure Jin; its contents are unknown.",
    "J1 was wiped out in a bizarre attack, leaving Yamamoto as its sole survivor; the bodies recovered afterward were severely desiccated despite having been dead less than two hours.",
    "Rumors about the J1 bodies are spreading among the assembled Hunters and rapidly undermining morale.",
    "Jin is setting out immediately to pursue The Prophet using the message sent through Yamamoto, even if it is a trap.",
    "The Skeleton King's memories from before he regained consciousness in a Gate are limited to a dark, ominous place; he does not know The Prophet.",
    "Magic Johnson has never encountered The Prophet's kind of ability and considers it possible The Prophet is an unidentified top-level Named monster.",
    "Amir and Hamid lead a group concealed by an unseen veil near a convoy of more than five hundred people; Amir orders them to await The Prophet and the coming holy war."
  ],
  "continuity_sources": [
    799,
    800
  ],
  "open_questions": [
    "What message did The Prophet leave for Jin, and where is The Prophet now?",
    "What is The Prophet's identity and power, and what was the pale mist absorbed from the J1 victims?",
    "Why did The Prophet spare Yamamoto, and what happened when Yamamoto tried to flee?",
    "Where is Amir’s concealed group, and what is its intended target?"
  ],
  "safe_through": 800,
  "temporary_decisions": [
    "Keep magic distinct from mana.",
    "Render 조센징 as “Chōsenjin,” identifying it as an ethnic slur."
  ],
  "version": 1
}
```

## Exact glossary matches

| 허준     | **Heo Jun**        |
| 일신     | **One God**         |
| 헌터      | **Hunter**            |
| 게이트     | **Gate**              |
| 팀장      | **Team Leader**       |
| 힐러      | **healer**            |
| 마정석     | **Magic Gem**         |
| 대격변     | **Great Cataclysm**   |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 필릭스 | **Felix** | British prince and S-rank Hunter. |
| 선지자 | **The Prophet** | Mysterious religious leader directing the terrorist warriors. |
| 야마모토 | **Yamamoto** | Japanese S-rank Hunter named in post-Leviathan media coverage. |
| 대한민국 | **Korea** | Country reference. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 피어 | **Fear** | Monster effect that overwhelms a target’s mental fortitude. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 스켈레톤 | **Skeleton** | Undead monster species. |
| 존슨 | **Johnson** | Co-host of the American talk show that replays Taekyung's viral interview. |
| 암초 | **reef** | Reefs blocking the narrow water route. |
| 아프리카 | **Africa** | Region where terrorist organizations are reportedly conducting Gate and Magic Gem experiments. |
| 중동 | **Middle East** | Region associated with the terrorist group and reported experiments. |
| 가기 | **singing courtesan** | The favored entertainer identity Honglan used in Hubei. |
| 재생 | **Regeneration** | The masked man's rapid recovery from shattered bones and severe wounds. |
| 변이 | **mutation** | The transformation threatening the humans and beasts in the Inner Palace. |
| 마력 | **magical power** | Distinct from mana; the Skeleton King's area of expertise. |
| 마정 | **Magic Gem** | Monster power source; Leviathan seeks an untouched one. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 필릭스 | 존슨 | prince_to_allied_grand_mage | Mr. Johnson | formal-polite | Felix uses a respectful address while speaking with Magic Johnson. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 800
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Felix.md

# Felix (필릭스)

- **Safe through:** Chapter 797
- **Aliases:** Prince Felix
- **Role:** British prince and S-rank Hunter who joins the reinforcement force against the Arch Lich.
- **Personality:** Haughty and conscious of royal duty, but increasingly willing to set aside convention and connect with allies as equals.
- **Voice:** Formal, lofty, and aristocratic.
- **Relationships:** Travels with Faye Chen and Magic Johnson and is allied with Jin Taekyung.

### Heo Jun.md

# Heo Jun (허준)

- **Safe through:** Chapter 408
- **Aliases:** Uncle Heo, Chief Escort
- **Role:** Former Chief Escort of the Yongbong Escort Bureau and Ju Hwaran's uncle, Heo Jun secretly colluded with Zhongnan for two years before Ju Hwaran exposed his betrayal and killed him with a sword strike.
- **Personality:** Deceitful, greedy, manipulative, and fiercely self-preserving beneath a long-maintained paternal facade.
- **Voice:** Formal, paternal, calm, and quietly reassuring.
- **Relationships:** He is Ju Hwaran's uncle and former Chief Escort, but his two-year betrayal of her and the Yongbong Escort Bureau has shattered their bond.

### The Prophet.md

# The Prophet (선지자)

- **Safe through:** Chapter 800
- **Aliases:** Muninn (무닌)
- **Role:** The Prophet is a monster posing as the leader of the revived Hasasin, whose power includes stopping transport vehicles and absorbing blood and a pale mist from the dead.
- **Personality:** Religiously fervent, commanding, and shrouded in an intentionally indistinct identity.
- **Voice:** Mysterious, genderless, and age-indeterminate, speaking in solemn religious imperatives.
- **Relationships:** The Prophet commands the ten warriors, is revered by the followers, and secretly communicates with Michael Silbert through a magic mirror.

### Yamamoto.md

# Yamamoto (야마모토)

- **Safe through:** Chapter 800
- **Aliases:** None
- **Role:** Yamamoto Genji is a Japanese S-rank Hunter and J1’s sole survivor.
- **Personality:** Prideful and easily offended, prone to self-aggrandizement and self-serving assumptions, and cowardly under mortal threat.
- **Voice:** Not established.
- **Relationships:** Jin Taekyung sent Yamamoto on the J1 mission and treated him after the attack, though Jin resents Yamamoto for arriving late during the Leviathan crisis.

## Korean source

```text
＃801화



“곧 출발할 거야. 준비해.”

다시 찾아와 불쑥 건넨 그 한 마디에, 야마모토 겐지는 의외로 고분고분하게 고개를 끄덕였다.

“알겠습니다.”

처음 깨어났을 때만 해도 조센징 운운하던 놈치고는 더할 나위 없이 공손한 태도다.

만약 허준이 이 놀라운 변화를 목격했다면, 동의보감의 첫 줄에 이렇게 적었을지도 몰랐다.

[매가 약이다.]

자고로 육신의 상처는 포션으로, 썩어 빠진 정신머리는 주먹으로 해결해야 하는 법.

후다닥 침대에서 일어난 야마모토 겐지가 훈련병처럼 차렷 자세를 취했다.

“준비 끝났습니다.”

“벌써?”

“하잇.”

“그 복장으로 싸우게?”

“엣?”

야마모토 겐지가 눈을 깜빡였다. 저 순진무구한 표정을 보아하니, 이 상황 자체를 이해하지 못한 것이 분명했다. 아니면 아예 제대로 듣지 못했거나.

그래서 친절하게 다시 말해 줬다.

“환자복 입고 싸울 생각이냐고.”

“……!”

짧은 침묵.

마침내 내가 말한 출발의 의미를 깨달은 야마모토 겐지가 떨리는 목소리로 물었다.

“저, 전장으로 가는 겁니까?”

“그럼 어디 가는 줄 알았는데.”

“저야 아직 환자니까 당연히 본대로 후송될 거라고 생각…….”

“후송?”

“하, 하잇.”

“음. 그래. 아직 환자구나, 환자.”

세상에. 그 중요한 걸 깜빡했네.

작게 중얼거린 나는 굳게 닫혀 있던 문을 걷어찼다.

“거기, 밖에 누구 없나?”

말이 떨어지기 무섭게 의무대에 소속된 힐러 한 사람이 빠릿빠릿하게 뛰어왔다.

“Yes, Sir.”

“그 뭐야. 아직 본대로 가는 후송 차량 출발 안 했죠?”

“예, 아직 대기 중입니다.”

“다행이네. 거기 팀장한테 바로 연락해서 한 구만 더 싣고 가라고 해요, 뒷수습은 내가 깔끔하게 해 줄 테니까 와서 들고 가기만 하면 될 거야.”

“그렇게 전달하겠습니다.”

“……잠깐만.”

오가는 대화를 듣고 있던 야마모토 겐지가 불길함이 감도는 얼굴로 물었다.

“한 구? 뒷수습? 그게 무슨 뜻입니까?”

“별거 아냐. 신경 쓰지 마.”

“엄청나게 별거인 것 같은데요. 거기, 당신. 폰 내려놔. 지금 누구한테 연락하는 거지?”

힐러가 무뚝뚝하게 대답했다.

“보스 지시대로 존스 팀장한테 연락 중입니다만.”

“존스 팀장이 누군데.”

“시신 수습을 전담하는 분입니다. 본대로 전사자들을 후송하시는.”

“……!”

나와 힐러를 번갈아 바라보던 야마모토 겐지가 결연한 표정으로 입을 열었다.

“사무라이의 명예를 걸고, 이 한목숨 바쳐 싸우겠습니다.”

“너한테 명예가 어디 있냐. 인터넷 보니까 별명이 질풍불참이던데.”

“…….”

“개소리 그만하고 장구류 갖춰서 나와.”

“옙. 그런데 혹시…….”

“혹시 뭐.”

“아직 몸이 안 좋아서 그러는데 정말 후방으로 빼 주실 수 없는…….”

빡!

“억!”

지금 같은 상황에서도 내뺄 생각만 하다니, 역시 이런 새끼는 좀 맞아야 한다.

한숨을 푹 내쉰 나는 비틀비틀 몸을 일으키는 놈을 바라보았다.

마음 같아서는 속 시원하게 두들겨 패고 싶은데, 저런 개똥 같은 놈이라도 필요하다는 사실이 기분을 더럽게 만들었다.

“야.”

“왜, 왜 그러십니까.”

“안 때릴 거니까 쫄지 마. 그냥 다시 한번 확인하려고.”

내가 착 가라앉은 목소리로 말을 이었다.

“그때 놈이 했다는 그 말. 확실해?”

그리고 야마모토 겐지가 입을 열기도 전에, 내 귓가에는 이미 몇 번이나 들었던 그 한 마디가 다시 한번 반복 재생되고 있었다.



‘룹 알 할리(Rub' al Khali). 더 늦기 전에 검은 보석이 잠든 땅으로 나를 찾아와라.’



선지자의 긴 로브 자락이, 금세라도 손에 잡힐 듯했다.



* * *



중동 대부분을 차지하는 아라비아 사막은 예맨에서부터 오만, 페르시아만을 거쳐 요르단과 이라크에까지 걸쳐 있다.

무려 230만 킬로미터가 넘는 광활한 면적.

UN에 제출된 대한민국의 공식 면적이 20만 킬로미터를 약간 웃도는 것을 생각한다면, 그야말로 미친 수준이 아닐 수 없다.

‘이런 넓은 땅을 샅샅이 뒤지려고 했으니 그렇게 예상 시간이 길게 나왔지.’

하지만 별다른 방법이 없었다.

나날이 상승세를 찍는 마나 분포도와 짙은 농도 앞에서는 최첨단 기기조차 제 기능을 발휘하지 못했고, 이 면적을 커버하려면 10만 명의 헌터가 발로 뛰어다니는 수밖에.

다만 다행인지 불행인지 헷갈리는 한 가지 사실은…… 바로 이 드넓은 사막 어딘가에 숨어 있던 선지자가 스스로 한 장소를 지목했다는 것이다.

룹 알 할리 사막.

아라비아 사막이 중동 전체의 사막 지대를 포함하는 큰 틀이라면, 중심부에 자리 잡은 그곳은 아라비아 반도 남부에 펼쳐져 있는 거대한 사막이다.

아프리카 대륙에 존재하는 사하라 사막에 이어 전 세계에서 두 번째로 넓은 사막이었지만, 선지자가 남긴 말에서 특정 범위를 유추해 내는 것은 그리 어렵지 않았다.

적어도 최 팀장에게는.

“공백 지대.”

“그게 뭡니까?”

“룹 알 할리(الربع الخالي‎)는 아라비아어로 공백 지대라는 뜻이더군요. 누구도 살지 못하는 땅. 뜨거운 햇빛과 모래만이 있는 땅. 그래서 그처럼 황량한 이름이 붙었을 겁니다.”

“그럼 검은 보석이라는 건…….”

“유전(油田)이 있습니다. 과거에는 전 세계에서 가장 큰 규모였다던데…… 선지자가 남긴 말뜻을 유추해 보았을 때, 지금으로서는 그곳이 가장 유력한 장소인 듯합니다.”

어려운 것은 수색하는 과정이지, 이동 자체가 아니다. 한번 목적지를 정하자 진격 속도는 상상을 초월했다.

특히 이번 출정을 위해 선별된 천 명의 헌터들은 중동에 파견된 이들 중에서도 손꼽히는 정예였고, 우리는 최단 거리로 아라비아 사막을 가로질러 룹 알 할리 사막에 도착했다.

그리고 옛 중동인들이 왜 이 땅에 공백 지대라는 명칭을 붙였는지 곧장 깨달았다.

망망대해처럼 끝도 없이 펼쳐진 사막과 황야. 그 안에 암초처럼 드문드문 들어선 작은 마을들.

각종 기계와 버려진 공업 단지가 있는 그곳은 과거 세계 최대의 유전이 존재했던 곳이라는 사실이 믿기지 않을 만큼 황폐했다.

오죽하면 스켈레톤 킹조차 눈을 깜빡거리며 의문을 표할 정도였다.

“뭐야, 여기가 인간들이 사는 땅이라고? 게이트가 아니라?”

괜히 최 팀장이 ‘과거에는’이라는 표현을 앞에 붙였던 것이 아니었다.

이곳은 이미 두 번 버려진 땅이다.

먼 옛날 토착민들에 의해 ‘룹 알 할리’라는 이름이 붙여졌을 때 한 번. 대격변이라는 재앙 속에서 또 한 번.

그리고 버려진 데에는 다 이유가 있는 법이었다.

“환상적인데그래.”

저 말이 함께 온 매직 존슨이 한 말이었다면 좋았겠지만, 안타깝게도 목소리의 주인은 스켈레톤 킹이었고 그 이유는 나 역시 느끼고 있었다.

어쩌면 우리 모두가.

‘마력(魔力)의 농도가…… 너무 짙다.’

어느 순간부터 공기가 무거워졌다고 느낀 것은, 머리 위로 쏟아지는 햇빛 때문만은 아닐 것이다.

덜컹. 푸쉬익.

갑작스럽게 꺼지는 시동. 천 명이나 되는 병력을 태운 채 달려가던 차량이 일제히 멈추자, 매직 존슨이 작게 중얼거렸다.

“슬슬 시작됐군.”

단순한 고장은 당연히 말도 안 되는 소리다.

앞서 비슷한 상황을 겪어 본 야마모토 겐지는 이미 얼굴이 새하얗게 질려 있었다.

“그가 왔어. 그가 왔어. 그가 왔어…….”

쉴 새 없이 중얼거리는 놈을 말없이 바라보던 스켈레톤 킹이 내게 물었다.

“저 인간, 죽여도 되나?”

“아니. 안타깝게도 안 돼.”

“왜? 어차피 몸으로 때우게 하려고 데려온 것 아닌가. 저 꼴을 계속 볼 바에는 차라리 언데드로 만들어도 괜찮을 것 같은데.”

“오.”

이 새끼 혹시 천잰가.

제법 논리정연한 말에 고개를 끄덕일 뻔한 걸 겨우 참아 낸 나는 야마모토 겐지를 호되게 걷어찬 다음 차량에서 내렸다.

‘벌써 오긴 무슨.’

아직 선지자가 암시한 유전 지대까지는 상당한 거리가 남아 있을뿐더러, 마력 농도가 짙어진 것을 제외하면 별다른 무언가를 느끼지도 못했다.

이건 그저 징조다.

이 드넓은 사막 어딘가에 아직 조우하지 못한 무언가가 있다는, 불길하지만 확실한 징조.

곧이어 정해진 시간마다 마력 분포도를 체크하던 측정 계원의 보고를 듣고 짐작은 확신으로 굳혀졌다.

“측정 불가입니다. 저희가 보유한 기기로는 정확한 수치를 파악하기 어렵습니다.”

그 귀한 A급 마정석을 몇 개나 박아 넣은 측정 기기로도 불가능하다니.

나는 마른 입술을 핥으며 중얼거렸다.

“찾으러 오라더니, 그냥 던져 본 헛소리는 아니었나 보네.”

조용히 옆으로 다가온 최 팀장이 입을 열었다.

“지금이라도 병력을 뒤로 물리고 추가 지원 요청을 할까요?”

최 팀장다운 신중한 제안이었지만, 나는 별다른 망설임 없이 고개를 저었다.

“아뇨. 이대로 계속 갑니다.”

“어떤 함정이 기다리고 있을지 모릅니다.”

“당연히 그럴 가능성은 충분하죠. 선지자, 그 새끼가 어떤 새낀데.”

“그럼 어째서.”

“함정이 있더라도 뚫고 가야 합니다. 우리한테는 시간이 없어요. 그리고…….”

문득 목소리를 낮춘 내가 말을 이었다.

“만약 선지자의 목적이 유인 그 자체에 있다면, 더더욱 지원 요청을 해서는 안 되죠.”

선지자의 능력도, 일신의 무력도 어디까지인지 밝혀지지 않았다.

그런데 이런 상황에서 핵심 전력이라 할 수 있는 S급 헌터를 이곳으로 호출한다면 남아 있는 병력이 위태로워진다.

이 사막에서 선지자는 수많은 광신도를 거느린 교황(敎皇)이나 다름없는 존재니까.

‘병력이라도 충원했다가 빈집털이라도 당하면 곤란하지.’

물론 그렇다고 해서 무모하게 싸울 생각도 없다.

평소였다면 단신으로 움직였을 내가 굳이 일천이나 되는 병력을 이끌고 온 것도 그 때문이다.

아무리 강하다 해도 나는 무적이 아니고, 밝혀지지 않은 적만큼 위험한 것도 없으니까.

그리고 그런 의미에서 지금 우리가 갖춘 전력은 부족하지도, 과하지도 않았다.

나를 제외하고서라도 매직 존슨과 스켈레톤 킹이라는 든든한 강자들이 있다. 거기에 더해 겁쟁이긴 해도 야마모토 겐지와 최 팀장까지 있으니, 어떤 상황이 찾아오더라도 깨부수며 나아갈 수 있을 거라고 확신했다.

‘여기서 병력을 충원한다면, 놈이 도망칠 수도 있다.’

전방에는 우리가, 후방에는 척 헤이글과 파이 첸, 필릭스 왕자를 비롯한 몇몇 S급 헌터가 상당한 전력을 이끌고 포위망을 지키고 있다.

여기에서 조금이라도 더하거나 덜어낸다면 힘의 저울추가 기울고 선지자를 처치할 기회 역시 그만큼 멀어질 수밖에 없다.

“어떤 맹수도 자신보다 강해 보이는 상대에게는 덤벼들지 않아. 선지자처럼 여우 같은 놈이라면 더더욱. 안 그래, 진?”

“맞습니다.”

매직 존슨의 말에 고개를 끄덕인 나는, 저 멀리 사막 위로 피어오르는 아지랑이를 바라보며 나직이 말을 이었다.

“그래도 다행이네요. 그 눈치 빠른 여우가, 이대로 겁먹고 도망치진 않은 것 같아서.”

“그게 무……!”

찰나의 순간 딱딱하게 굳어 버린 얼굴.

내 말의 의미를 깨닫고 황급히 뒷말을 삼킨 매직 존슨이, 강대한 마나를 실어 외쳤다.

“전투 준비!”

그래.

놈들이 오고 있다.
```

## Final English reading copy

```markdown
# Chapter 801

“We’re leaving soon. Get ready.”

At that one remark, tossed out when I came back without warning, Yamamoto Genji surprisingly nodded obediently.

“Understood.”

For a guy who’d been going on about Chōsenjin when he first woke up, he was being about as polite as possible.

If Heo Jun had witnessed this astonishing change, he might have written this on the first line of the *Donguibogam*:

> A beating is the best medicine.

As a rule, you treat wounds on the body with potions and rotten minds with your fists.

Yamamoto Genji sprang out of bed in a hurry and snapped to attention like a trainee.

“I’m ready.”

“Already?”

“Yes, sir.”

“You planning to fight in that?”

“Huh?”

Yamamoto Genji blinked. Judging by that utterly innocent expression, he clearly didn’t understand what was going on. Or maybe he hadn’t heard me properly at all.

So I kindly repeated myself.

“You planning to fight in your hospital gown?”

“……!”

A brief silence.

At last, Yamamoto Genji understood what I meant by *leaving* and asked in a trembling voice,

“W-we’re going to the battlefield?”

“Where did you think we were going?”

“I assumed that, since I’m still a patient, I’d naturally be sent back to the main camp…”

“Sent back?”

“Y-yes, sir.”

“Hmm. Right. You’re still a patient, aren’t you? A patient.”

Good grief. I’d forgotten something important.

Muttering under my breath, I kicked open the firmly shut door.

“Hey! Anyone out there?”

Before the words had even left my mouth, a healer from the medical unit came running over.

“Yes, sir.”

“Um, what was it? The transport vehicle going back to the main camp hasn’t left yet, right?”

“That’s right. It’s still waiting.”

“Good. Contact the team leader right away and tell him to load one more body. I’ll take care of the cleanup, so all they have to do is come pick him up.”

“I’ll pass that along.”

“……Wait a second.”

Yamamoto Genji, who’d been listening to our conversation, asked with a foreboding look on his face,

“One more body? Cleanup? What does that mean?”

“It’s nothing. Don’t worry about it.”

“It sounds like a pretty big deal. Hey, you. Put down the phone. Who are you calling?”

The healer replied bluntly,

“I’m contacting Team Leader Jones, as the boss instructed.”

“Who’s Team Leader Jones?”

“He’s in charge of recovering the dead. He transports the fallen back to the main camp.”

“……!”

Yamamoto Genji looked back and forth between me and the healer, then spoke with a resolute expression.

“On the honor of a samurai, I’ll give my life and fight.”

“What honor? I looked you up online. Your nickname is ‘Swift No-Show.’”

“……”

“Quit talking bullshit and gear up. Get out here.”

“Yes, sir. But, by any chance…”

“What?”

“I’m still not feeling well, so could you really send me to the rear…”

*Whack!*

“Ugh!”

Even at a time like this, he was still thinking about running away. A bastard like this needed a little beating.

I let out a deep sigh and watched him stagger back to his feet.

I wanted nothing more than to beat the hell out of him, but the fact that I needed even a piece of shit like him made me feel even worse.

“Hey.”

“Y-yes? What is it?”

“I’m not going to hit you, so don’t freak out. I just want to make sure one more time.”

My voice low, I continued,

“What you said he told you back then. Are you sure?”

Before Yamamoto Genji could open his mouth, the same words I’d heard several times already replayed in my ears.

> “Rub’ al Khali. Come find me in the land where the black jewel sleeps, before it’s too late.”

The trailing hem of The Prophet’s long robe seemed close enough to reach out and grab.

* * *

The Arabian Desert covers most of the Middle East, stretching from Yemen through Oman and the Persian Gulf, as far as Jordan and Iraq.

An immense expanse, more than 2.3 million square kilometers.

Korea’s official area, as submitted to the UN, was just over 200,000 square kilometers. Compared to that, this place was simply insane.

*No wonder the estimated search time was so long. We were planning to comb an area this huge from end to end.*

But we didn’t have many options.

With mana levels rising by the day and concentrations growing denser, even the most advanced equipment couldn’t function properly. The only way to cover an area this large was to send a hundred thousand Hunters out on foot.

There was one fact that was hard to decide whether it was fortunate or unfortunate, though…

The Prophet, who’d been hiding somewhere in this vast desert, had singled out a location for us.

The Rub’ al Khali Desert.

If the Arabian Desert was the broad term for the desert regions covering the entire Middle East, then the Rub’ al Khali, in its center, was a vast desert stretching across the southern Arabian Peninsula.

It was the second-largest desert in the world, after the Sahara in Africa. Still, it wasn’t difficult to guess the specific area The Prophet had meant.

At least, not for Team Leader Choi.

“The Empty Quarter.”

“What’s that?”

“Rub’ al Khali means ‘Empty Quarter’ in Arabic. A land where no one can live. A land of nothing but blazing sunlight and sand. That must be why it was given such a desolate name.”

“Then the black jewel must mean…”

“There are oil fields there. They were supposedly once the largest in the world… Judging from The Prophet’s message, that seems like the likeliest place now.”

The hard part was searching, not getting there. Once we’d chosen our destination, our advance moved at an astonishing speed.

The thousand Hunters selected for this expedition were among the very best of those deployed to the Middle East. We crossed the Arabian Desert by the shortest route and arrived at the Rub’ al Khali.

And we immediately understood why the people of the ancient Middle East had called this place the Empty Quarter.

An endless desert and wilderness spread out like a vast ocean, dotted with small villages as sparse as reefs.

With its machinery and abandoned industrial complexes, the place looked so desolate it was hard to believe the world’s largest oil field had once been there.

It was bleak enough to make even the Skeleton King blink in confusion.

“What? This is a place where humans live? Not a Gate?”

There was a reason Team Leader Choi had used the words *once was*.

This land had already been abandoned twice.

Once, long ago, when the natives named it the Rub’ al Khali. And once again, amid the calamity known as the Great Cataclysm.

There was always a reason a place got abandoned.

“Spectacular.”

I wish those words had come from Magic Johnson, who’d come with us. Unfortunately, the voice belonged to the Skeleton King—and I felt the same way he did.

Maybe we all did.

*The concentration of magical power… It’s too dense.*

The air had started feeling heavy at some point, and it wasn’t just because of the sunlight pouring down on us.

*Clunk. Psssh.*

An engine abruptly died. As the vehicles carrying a thousand soldiers all came to a halt, Magic Johnson murmured,

“It’s starting.”

There was no way this was a simple mechanical failure.

Yamamoto Genji, who’d already experienced something similar, had gone deathly pale.

“He’s here. He’s here. He’s here…”

The Skeleton King watched him mutter without pause, then asked me,

“Can I kill that human?”

“No. Unfortunately, you can’t.”

“Why not? Didn’t we bring him along to put his body to use? If we have to keep looking at him like that, turning him into an undead might be better.”

“Oh.”

Was this bastard a genius?

I barely stopped myself from nodding at his surprisingly logical argument. Then I gave Yamamoto Genji a hard kick and got out of the vehicle.

*What do you mean, he’s here already?*

We were still a considerable distance from the oil fields The Prophet had hinted at. And other than the rising concentration of magical power, I hadn’t sensed anything unusual.

This was only a sign.

An ominous but certain sign that something we hadn’t encountered yet was somewhere in this vast desert.

Soon, a report from the measurement specialist, who was checking the magical-power distribution at regular intervals, turned my suspicion into certainty.

“We can’t get a reading. Our equipment can’t determine an accurate value.”

Even the measuring device, which had several precious A-rank Magic Gems installed in it, couldn’t do it.

I licked my dry lips and muttered,

“He told us to come find him. Guess it wasn’t just some bullshit he threw out there.”

Team Leader Choi stepped quietly up beside me and spoke.

“Should we pull our forces back and request reinforcements while we still can?”

It was a cautious suggestion, very much like Team Leader Choi. But I shook my head without hesitation.

“No. We keep moving.”

“We don’t know what kind of trap might be waiting for us.”

“Of course that’s a real possibility. You know what that bastard Prophet is like.”

“Then why…”

“Even if there’s a trap, we have to break through it. We don’t have time. And…”

Lowering my voice, I continued,

“If The Prophet’s real goal is to lure us out, then all the more reason not to request reinforcements.”

We still didn’t know the limits of The Prophet’s abilities or personal fighting strength.

But if we called an S-rank Hunter—a key part of our strength—here under these circumstances, the forces left behind would be in danger.

In this desert, The Prophet was practically a pope commanding countless fanatics.

*It’d be a problem if we brought in reinforcements only to leave the rear wide open to a raid.*

That didn’t mean I planned to fight recklessly, of course.

Under normal circumstances, I would’ve gone alone. The reason I’d brought a thousand soldiers was precisely this.

No matter how strong I was, I wasn’t invincible. And nothing was as dangerous as an enemy whose abilities were unknown.

In that sense, the force we’d assembled was neither insufficient nor excessive.

Even without me, we had two dependable powerhouses in Magic Johnson and the Skeleton King. Add the cowardly Yamamoto Genji and Team Leader Choi, and I was sure we could smash our way through whatever came.

*If we bring in more forces, he might run.*

Chuck Hagel, Faye Chen, Prince Felix, and several other S-rank Hunters were guarding the encirclement with a considerable force to our rear.

If we added or removed even a little from either side, the balance of power would shift—and our chance to eliminate The Prophet would slip that much farther away.

“No beast ever attacks an opponent that looks stronger than it is. Especially not a fox like The Prophet. Right, Jin?”

“That’s right.”

I nodded at Magic Johnson and looked at the heat haze rising over the distant desert.

“Still, that’s a relief. Looks like that quick-witted fox hasn’t gotten scared and run off.”

“What do you mean—!”

His face went rigid in an instant.

Realizing what I meant, Magic Johnson hurriedly swallowed the rest of his words and shouted, pouring his mighty mana into his voice.

“Prepare for battle!”

Right.

They were coming.
```
