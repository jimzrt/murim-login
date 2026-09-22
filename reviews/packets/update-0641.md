<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0641.txt",
      "sha256": "cdef1a5e15d12adb33bfd1a171fb56777a7e9f5288f97f42d0ec32d5b4b6226a",
      "bytes": 12723
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "e3f110c4a7a1d7025aa5edead2c4e034ca83e133e4660e04322073d56dfe72cb",
      "bytes": 1328
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "2e54c7fa9b2504231369591cadd144fe1f3d21672db80e5ee729597516271371",
      "bytes": 197596
    },
    {
      "path": "characters/Beast Miao King.md",
      "sha256": "2994afb49a891cf7152186e9e7252542ced5ec7040be881ceaf1ef0d09691ea1",
      "bytes": 560
    },
    {
      "path": "characters/Jang Sam.md",
      "sha256": "3ccf40c4db89c70467d891649e6c880164dbcb30b2e454af0cabcd74d85835d0",
      "bytes": 408
    },
    {
      "path": "characters/Pill Physician.md",
      "sha256": "df9003371e7ce7db314a300dc9311f48865f80db0300fd5374d596cd2b0691e2",
      "bytes": 554
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2ee77e9a1d5d7d04bc6461137b6bdb37bcf4edf48b220c849a97822225533a4e",
      "bytes": 202599
    }
  ],
  "estimated_tokens": 8761
}
-->

# Durable State Update — Chapter 641

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 641. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 641. Profile updates may replace only one
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
  "chapter": 641,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 641,
    "continuity_sources": [641],
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
    "The Level 119 Thousand-Year Spider was killed by Jin Taekyung after the Beast Miao King brought it to him.",
    "Jin’s level-up cleared the status abnormalities caused by One Annihilation and substantially restored his body, though he still needs treatment and rest.",
    "Jin Taekyung and the Beast Miao King are advancing deeper into the Poisonblood Grounds.",
    "Ailao Mountain’s Wraith remains in the Poisonblood Grounds and is the main threat despite not joining the earlier battles.",
    "Jin carries guilt over the massacre of Nanman warriors and considers whether that burden is a Heart Demon.",
    "A vast moonlit swamp contains many transparent web-wrapped objects and pure-white eggs."
  ],
  "continuity_sources": [
    640
  ],
  "open_questions": [
    "What are the objects wrapped in transparent spiderwebs in the swamp?",
    "What are the pure-white eggs, and what will emerge from them?",
    "Why has Ailao Mountain’s Wraith not attacked Jin Taekyung and the Beast Miao King?",
    "What does Ailao Mountain’s Wraith intend to do?"
  ],
  "safe_through": 640,
  "temporary_decisions": [
    "Use Sword Demon for 검마.",
    "Use two-headed horn snake for 쌍두각사.",
    "Use black frog for 흑와.",
    "Use golden bee for 금봉."
  ],
  "version": 1
}
```

## Exact glossary matches

| 장삼 | **Jang Sam** | Bandit; personal name |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 환의 | **Pill Physician** | Title of the current Family Head of the Seongsu Jang Family. |
| 평화 | **Peace Guild** | Guild name. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 천마 | **Heavenly Demon** | Demonic title used in Jeok Cheongang's impossible comparison. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 마도 | **Demonic Path** | Term raised for martial power that appears to defy common principles. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 무형지독 | **Formless Ultimate Poison** | Unidentified poison discovered inside Jeok Cheongang's body. |
| 만독지환 | **Myriad-Poison Ring** | Quest title concerning a legendary treasure said to detoxify any poison. |
| 피독주 | **poison-warding pearl** | Poison-neutralizing artifact carried by the black-clad attackers. |
| 푸린 | **Furin** | Russian president mentioned in a forum headline. |
| 남천마후 | **Southern Heaven Demon Empress** | Title Honglan uses when revealing her identity. |
| 오독문 | **Five Poisons Sect** | Formerly dominant Nanman faction destroyed by the Fire Gate Clan. |
| 황하 | **Yellow River** | River along which civilization began. |
| 이전 | **Two Halls** | Top-level Murim Alliance organizational grouping. |
| 독물 | **venomous beasts** | Venomous creatures associated with the Nanman Beast Palace. |
| 마비 | **Paralyzed** | Status abnormality inflicted by Kraken's Ink. |
| 제니 | **Jenny** | East Asian news anchor interviewing Jacob. |
| 남천 | **South Heaven** | Dark Heaven power that the Lord of Heaven orders the servants to contact. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |
| 무야호 | **Muyaho** | Yayul Mok's White Tiger's name; it means tiger of the mighty wilds. |
| 독혈지 | **Poisonblood Grounds** | Hidden poisonous region created by the Five Poisons Sect inside Ailao Mountain. |
| 독무 | **Poison Mist** | Deep green mist covering the Poisonblood Grounds swamp. |
| 천년지주 | **Thousand-Year Spider** | Monster appearing at the end of the chapter. |

## Matched address pairs

(No matching address pairs.)

## Listed compact profiles

### Beast Miao King.md

# Beast Miao King (야수묘왕)

- **Safe through:** Chapter 640
- **Aliases:** None
- **Role:** The Beast Miao King is the Palace Lord of the Nanman Beast Palace, the great chieftain of the Miao people, and a master among the Ten Kings.
- **Personality:** Fierce and vigilant when confronting threats to the Nanman Beast Palace.
- **Voice:** Low, growling, and forceful.
- **Relationships:** He commands the Nanman Beast Palace and is responsible for the forces stationed at Ailao Mountain.

### Jang Sam.md

# Jang Sam (장삼)

- **Safe through:** Chapter 617
- **Aliases:** Killing Ghost
- **Role:** Jang Sam was a Hubei fisherman who disappeared for a month and reappeared as a grotesque mutant monster known as a Killing Ghost.
- **Personality:** Not established.
- **Voice:** Not established.
- **Relationships:** No relationships established.

### Pill Physician.md

# Pill Physician (환의)

- **Safe through:** Chapter 508
- **Aliases:** None
- **Role:** Current Family Head of the Seongsu Jang Family in Shandong, who personally placed and signed the Thousand-Year Snow Ginseng in the casket entrusted to the Yongbong Escort Bureau.
- **Personality:** No personality traits are established.
- **Voice:** No voice traits are established.
- **Relationships:** The Pill Physician heads the Seongsu Jang Family, a prestigious medical family in Shandong.

## Korean source

```text
＃641화



간혹 그런 순간이 있다. 단지 어떤 것을 목격한 것만으로도 등골이 오싹해지고, 모골이 송연해지는 순간이.

지금 내 눈앞에 보이는 모든 풍경처럼.

스아아.

흔들리는 나뭇잎 사이로 쏟아지는 희미한 달빛은 신화 속 한 장면처럼 신비로웠지만, 그 달빛이 비치고 있는 것은 평화로운 푸른 호수가 아니었다.

‘이건…….’

어둠과 스산함이 깃든 늪지. 그리고 마치 누에고치처럼 거미줄에 겹겹이 감싸인 수백여 개의 커다란 형체들과 그보다는 작지만 몇 배나 많은 새하얀 알들.

‘도대체 뭐지?’

답을 알아서는 안 될 것 같은 불길한 의문이 마음을 짓누른다.

하지만 그런 생각과는 반대로, 본능적으로 내뻗은 손은 이미 가장 가까운 곳에 매달린 정체불명의 누에고치를 건드리고 있었다.

툭.

손가락 끝을 통해 전해지는 불쾌한 촉감. 그와 동시에 시스템 알림이 귓가를 파고들었다.

삐빅. 띠링.



- [천년지주의 마비 독]에 중독되셨습니다!

- 신속하게 해독하지 않을 시 [전신 마비]와 [의식 불명] 상태에 이를 수 있습니다!

- [만독지환]의 잠재 효과가 발동되었습니다!

- [독]과 관련된 모든 상태 이상이 해제됩니다!



잠깐 얼얼해지나 싶던 손가락 끝이 시원해진다.

만독지환은 무형지독 마저 흡수하는 신물(神物). 천년지주가 아무리 특별한 독물이라 하더라도 나를 어찌할 수는 없었다.

‘그나저나 이게 천년지주의 거미줄이라면…….’

문득 한 가지 짐작이 뇌리를 스친다. 나는 손에 한층 힘을 실어 거미줄을 좌우로 잡아 뜯었다.

콰득. 지지직.

수백 겹으로 뭉쳐져 있던 거미줄이 무시무시한 악력에 힘없이 찢겨 나간다.

그리고 그 안에 감춰져 있던 무언가의 모습이 드러나자, 옆에서 지켜보던 야수묘왕이 신음처럼 중얼거렸다.

“사람?”

그의 말은 사실이었다.

백지장처럼 새하얗게 질린 얼굴과 한 치의 미동도 없는 몸.

거미줄 안에서 나타난 이름 모를 사내의 완맥(緩脈)을 짚은 야수묘왕이 안도의 한숨을 내쉬었다.

“다행이군. 아직 숨이 붙어 있다.”

나로서도 충분히 예상했던 부분이었다.

앞서 시스템이 알려 준 바에 의하면, 천년지주의 거미줄에는 대상을 절명(絶命)에 이르게까지 하는 독은 없었으니까.

그리고 그 이유는 아마도…….

‘신선도를 유지하기 위해서겠지. 그래야 놈들이 원할 때 배를 채울 수 있을 테니까.’

비로소 알겠다. 처음 이곳에 발을 디딘 순간, 왜 나도 모르게 모골이 송연해졌는지.

‘도축장.’

이 늪지는 천년지주가 머물던 거처이기 이전에, 하나의 도축장이며 거대한 식량 저장고다.

그제야 사방에서 풍겨 오는 악취에 가려져 있던 짙은 혈향(血香)을 알아차린 나는 작게 중얼거렸다.

“거미 새끼들. 오랫동안 많이도 해 처먹었네.”

수백. 아니, 어쩌면 수천.

과거 오독문이 독혈지를 만들었다는 남만야수궁의 기록이 사실이라면, 그 세월 동안 이곳에서 죽어 간 이들의 숫자는 헤아릴 수 없이 많을 것이다.

아이러니하게도 그런 천년지주의 습성 덕분에 오늘은 많은 이들을 살릴 수 있게 되었지만.

‘확실히 이상하긴 했지. 죽은 사람보다 사라진 이들이 더 많았으니까.’

애뇌산에 주둔하고 있던 정예들의 숫자는 총 삼백여 명이다.

다섯 마리의 천년지주는 그중 백여 명을 그 자리에서 죽이고, 적당히 허기를 채운 후 남은 이들을 독혈지로 끌고 온 것이 확실했다.

얼마 지나지 않아 차례대로 한 끼 식사가 됐을 그들을 지금 우리가 구하게 된 거고.

“이런 쳐 죽일 놈들을 봤나!”

나는 분노로 눈가가 붉게 달아오른 야수묘왕을 진정시켰다.

“그, 말씀 중에 죄송한데, 이미 쳐 죽이셨습니다.”

“찢어 죽여도 시원치 않다!”

“어…….”

그럼 또 내가 할 말이 없지. 하지만 당장은 분노하는 것보다 현재 상황을 수습하는 것에 집중해야 할 때다.

잠시 후 분노를 가라앉힌 야수묘왕은 참담한 표정으로 주위를 둘러보았다.

“감히 이런 짓을 벌이고 있었다니.”

“그러고 보니 지금까지는 큰 피해가 없었다고 하지 않았습니까?”

“틀림없는 사실이다. 적어도 내가 궁주로 있는 동안은 아무 문제도 없었어.”

“그거참 희한하네요. 갑자기 이런 시기에 천년지주가 다섯 마리나 나타나서 전사들을 습격하다니.”

다분히 의도가 묻어나는 내 말에 잠시 침묵하던 야수묘왕이 불쑥 입을 열었다.

“……암천(暗天). 놈들의 소행이라고 생각하느냐?”

나는 망설임 없이 고개를 끄덕였다.

“직접 손이 닿았는지는 몰라도 입김 정도는 불었을 겁니다. 독물인 천년지주가 사람을 습격하는 건 전혀 이상하지 않지만, 지금 같은 시기라면 당연히 그렇게 생각할 수밖에 없죠.”

“하지만 정말 암천의 소행이라면, 네가 떠난 뒤에 시작해도 늦지 않았을 것이다. 부족 대회의 마지막 날에 이런 짓을 벌이는 것이 놈들에게는 오히려 손해일 테니까.”

“그건…….”

나도 모르게 말꼬리가 흐려진다. 그만큼 야수묘왕이 내놓은 대답은 의외로 날카로웠고, 쉽게 부정할 수 없는 근거가 있었다.

‘틀린 말이 아니지. 만약 내가 남천마후, 그 썅년이었다면 굳이 이런 일을 벌이지 않았을 테니까.’

가만히 놔둬도 남만야수궁의 입맹(入盟)이 무산되는 것은 기정사실이나 다름없던 상황. 암천으로서는 괜히 남만을 들쑤실 이유가 없었다.

‘그런데 왜?’

모든 것이 의문투성이다.

갑작스럽게 나타나 지금까지도 모습을 보이지 않는 애뇌산의 망령. 난데없이 살육을 벌인 다섯 마리의 천년지주와 암천과의 연관성.

한동안 눈살을 찌푸린 채 생각에 잠겨 있던 나를 깨운 것은 야수묘왕의 목소리였다.

“그보다 당장은 이들을 옮기는 것이 문제다. 아직 숨이 붙어 있는 것은 천만다행이지만, 다시 독혈지를 빠져나가는 건 다른 문제니까.”

상념을 멈춘 내가 대답했다.

“제 생각을 말씀드리자면, 다른 사람들은 그대로 놔두는 게 나을 것 같은데요.”

“그대로? 이곳에 계속 말이냐?”

“……아니, 제가 무슨 미친놈입니까? 당연히 남만야수궁으로 데려가야죠. 백호에게 사람들을 데려오라고 했으니 기다리는 게 좋을 것 같습니다. 정말 알아들었는지는 모르겠지만.”

“무야호를 말하는 모양이군. 어지간한 사람보다 영특한 녀석이니 충분히 알아들었을 거다.”

“…….”

“표정이 왜 그러지?”

“아. 아닙니다. 아무것도.”

웃참 실패할 뻔.

무야호라니. 저 이름은 들으면 들을수록 적응이 안 되네. 무너지려는 표정을 간신히 수습한 내가 말을 이었다.

“그리고 거미줄은 뜯지 말고 그대로 놔두는 게 좋을 것 같습니다.”

“독 때문이군.”

“예.”

오는 길도 어려웠지만, 돌아가는 길은 훨씬 힘들 거다.

지난 몇 시진 동안 전신 마비와 의식불명 상태에 빠져 있다가 겨우 깨어난 환자 이백여 명과 함께 독무(毒霧)를 헤쳐 가야 할 테니까.

‘만독지환의 공능이 어디까지 커버할 수 있을지도 의문이고.’

만독지환은 분명히 신비한 힘을 지닌 신물이지만, 이것 하나만 믿고 이백 명의 목숨을 확률 절반짜리 가챠를 돌릴 수는 없다.

오히려 이대로 거미줄에 감겨 있는 것이 안전하지.

“저 안에 있으면 최소한 독무의 영향은 안 받는 것 같습니다. 만약 아니라면 이미 여기까지 오는 길에 다 죽었을걸요.”

“그도 그렇군. 거미줄에 스며있는 천년지주의 독이 다른 잡독을 막아 주는 것일지도 모르지.”

어떤 의미로는 이독제독(以毒制毒)과 비슷한 맥락이다.

오는 길에는 거미줄로 이루어진 관짝이었겠지만, 지금부터는 독무로부터 목숨을 지켜 줄 냉동 캡슐이다.

일일이 한 사람씩 꺼내서 해독시켜 봤자 내가 할 수 있는 것도 한계가 뚜렷한 편이고.

기껏해야 이런 대화 정도다.



‘자. 환자분. 천천히 눈 뜨세요. 지금 눈앞에서 흔들고 있는 제 손가락 보이세요? 보이시면 개수 말해 보세요.’

‘으으음. 하나, 하납니다.’

‘무슨 손가락인가요?’

‘중지요.’

‘네. 엿 먹으라는 뜻입니다.’

‘예? 갑자기 그게 무슨…….’

‘간단한 시험이었어요. 어쨌든 좋습니다. 이제 정확히 보고 들으시는군요. 시각과 청각 모두 회복됐어요.’

‘흑흑. 감사합니다. 정말 감사합니다, 한족 선생님.’

‘허허. 뭘요. 그나저나 해독했으니 마비가 풀렸을 텐데. 뭐 어떻게, 손가락은 움직일 수 있으신가요?’

‘물론입니다. 이제 충분히 움직일 수 있어요.’

‘그럼 이제부터 손가락을 좀 쓸 일이 있는데. 그전에 혹시 성함이?’

‘저요? 장삼입니다.’

‘좋습니다. 그럼 제가 이 단도를 드릴 테니까, 지금부터 이 목판에 제가 부르는 대로 써 보세요.’

‘예, 예.’

‘자. 지금부터 제가 부르는 대로 쓰시는 겁니다. 장삼.’

‘장. 삼.’

‘이곳에 잠들다.’

‘이곳에 잠들. 예?’

‘사실 당황하실까 봐 말씀을 안 드렸는데, 이제 곧 왔던 길을 돌아가야 합니다. 그런데 더 이상 피독주가 없어요. 아, 물론 저는 만독지환이 있어서 괜찮습니다.’

‘……!’

‘저는 ‘무적’입니다. 만독지환은 ‘신’이고.’



으음.

만독지환을 차지하기 위한 이백 대 일의 혈투가 벌어지겠구만.

어쩌면 이백 대 이일지도 모른다. 야수묘왕도 크고 아름다운 최상급 피독주를 갖고 있으니까.

“……왜 그런 표정으로 날 바라보는 거지?”

“별거 아닙니다.”

“혹시 암천이냐?”

“아뇨. 하늘 천인데요.”

내 대답에 야수묘왕이 정색했다.

“진짜 미친놈인가……?”

부장님이었으면 웃었을 텐데, 궁주님이라 안 먹히는 모양이다.

두 발로 걷는 천년지주를 보는 듯한 표정으로 나를 훑어본 야수묘왕은 거미줄에 휘감긴 전사들을 한곳에 모으기 시작했다.

서걱. 서걱.

곧게 편 수도(手刀)가 움직일 때마다 허공에 매달려 있던 이들이 차곡차곡 쌓인다.

그 숫자가 무려 이백. 짐작대로 애뇌산에서 사라진 전사들의 숫자와 거의 비슷했다.

‘잠깐. 맹수들은?’

야수묘왕을 도와 생존자들을 옮기던 나는, 잠시 잊고 있던 생각에 번쩍 고개를 들었다.

처음 애뇌산을 수색하며 느꼈던 의문 중 하나. 사라진 맹수들의 모습은 이곳 어디에도 보이지 않는다.

곧 그 사실을 알아차린 야수묘왕도 의아한 표정을 지었다.

“이상한 일이군. 맹수들의 모습이 보이지 않아.”

“혹시 맹수들이 겁이 많은 편입니까? 처음 보는 사람들을 만나면 꼬리를 말고 도망친다든지.”

“궁금해서 묻는 건데, 혹시 맹수 뜻을 모르나?”

알지. 사나울 맹. 짐승 수.

그래서 더 이상한 거다. 그토록 많은 맹수가 주인을 놔두고 어디로 도망치지는 않았을 테니까.

‘그렇다고 천년지주가 편식을 하는 것도 아닐 거고.’

이 부분은 내가 잘 안다. 7년 가까이 살았던 희망 고시원에는 희망보다 거미가 더 많았으니까.

나중에는 친밀감까지 느껴서 라면도 나눠 줬을 정도다.

‘그럼 도대체 어디로 간 거야?’

독혈지를 좀 더 수색해 봐야 알겠지만, 천년지주가 종류별로 식품을 나눠 보관할 만큼 꼼꼼한 성격은 아닐 것 같다.

그리고 나와 야수묘왕이 의문 가득한 시선으로 주위를 둘러보고 있던 그 순간.

바스락.

작은 소음과 함께, 십여 장 밖에서 희미한 기척이 느껴졌다.
```

## Final English reading copy

```markdown
# Chapter 641

Sometimes, there are moments when merely witnessing something is enough to send a chill down your spine and make your hair stand on end.

Like every scene unfolding before my eyes right now.

*Fwoosh.*

The faint moonlight pouring through the swaying leaves was as mysterious as a scene from a myth, but what it illuminated was not a peaceful blue lake.

*What the……*

A swamp steeped in darkness and desolation. Hundreds of enormous shapes, layered in spiderwebs like silkworm cocoons, and pure-white eggs that were smaller but several times more numerous.

*What the hell are they?*

An ominous question pressed down on my heart, as if it were something I wasn’t supposed to learn the answer to.

But contrary to that thought, the hand I had extended on instinct was already touching the unidentified cocoon hanging closest to me.

*Tap.*

An unpleasant sensation traveled through my fingertip. At the same time, a System notification pierced my ear.

*Beep. Ding.*

> **System**
>
> - You have been **Poisoned** by **Thousand-Year Spider’s Paralytic Venom**!
>
> - If you are not detoxified quickly, you may enter **Full-Body Paralysis** and **Unconsciousness**!
>
> - The potential effect of the **Myriad-Poison Ring** has been activated!
>
> - All status abnormalities related to **Poison** have been removed!

My fingertip, which had felt numb for a moment, soon grew cool and clear.

The Myriad-Poison Ring was a sacred artifact that could even absorb Formless Ultimate Poison. No matter how special a venomous creature the Thousand-Year Spider was, it couldn’t do anything to me.

*If these really are the Thousand-Year Spider’s webs……*

A guess suddenly flashed through my mind. I put more strength into my hands and pulled the webbing apart from side to side.

*Crack. Riiiiip.*

The hundreds of layers of tangled web tore helplessly under my terrifying grip.

And when the shape concealed inside was revealed, the Beast Miao King, who had been watching from beside me, muttered like he was groaning.

“Is that a person?”

He was right.

A face as white as a sheet of paper. A body that did not move even an inch.

The Beast Miao King checked the unknown man’s slow pulse and let out a sigh of relief.

“Fortunately, he’s still breathing.”

That was something I had expected as well.

According to what the System had told me earlier, the Thousand-Year Spider’s webs did not contain poison powerful enough to kill their victims.

And the reason was probably……

*To keep them fresh. That way, they can fill their bellies whenever they want.*

Now I understood why the hair on my body had risen the moment I first set foot here.

*A slaughterhouse.*

Before being the Thousand-Year Spider’s habitat, this swamp was a slaughterhouse—and a gigantic food storage facility.

Only then did I notice the deep scent of blood hidden beneath the stench drifting in from every direction. I muttered under my breath.

“Spider bastards. They’ve sure been stuffing their faces for a long time.”

Hundreds. No, perhaps thousands.

If the Nanman Beast Palace’s records claiming that the Five Poisons Sect had created the Poisonblood Grounds were true, then the number of people who had died here over all those years would be impossible to count.

Ironically, the Thousand-Year Spiders’ habits had made it possible for us to save a great many people today.

*It really was strange. More people had disappeared than died.*

There had been about three hundred elite warriors stationed at Ailao Mountain.

The five Thousand-Year Spiders had definitely killed around a hundred of them on the spot, then, after satisfying their hunger, dragged the rest to the Poisonblood Grounds.

Those people would have been turned into meals one by one before long, but now we had a chance to save them.

“Would you look at these goddamn bastards! They deserve to die!”

I calmed the Beast Miao King, whose eyes had reddened with fury.

“Uh, sorry to interrupt, but you already killed them.”

“Tearing them to pieces wouldn’t be enough!”

“Uh……”

Well, I had nothing to say to that. Still, this was a time to focus on dealing with the current situation rather than getting angry.

After calming down a little, the Beast Miao King looked around with a devastated expression.

“To think they dared to do something like this.”

“You said there hadn’t been any major losses until now, didn’t you?”

“That is the truth. At least while I have been the Palace Lord, there was never a problem.”

“That’s strange. Five Thousand-Year Spiders suddenly appeared and attacked the warriors at a time like this.”

The Beast Miao King fell silent for a moment at my clearly pointed words, then abruptly spoke.

“……Dark Heaven. Do you think this was their doing?”

I nodded without hesitation.

“I don’t know whether they directly laid a hand on this, but they must have exerted some influence. It isn’t strange for a venomous creature like the Thousand-Year Spider to attack people, but considering the timing, we can’t help but suspect them.”

“But if this truly was Dark Heaven’s doing, they could have waited until after you left. Causing this on the final day of the tribal competition would only harm them.”

“That…….”

My voice trailed off despite myself. The Beast Miao King’s answer had been sharper than expected, and he had offered evidence I couldn’t easily refute.

*He’s not wrong. If I were Southern Heaven Demon Empress—that bitch—I wouldn’t have gone to the trouble of doing this.*

Even without any interference, it was practically certain that the Nanman Beast Palace’s entry into the Murim Alliance would fall through. Dark Heaven had no reason to stir up Nanman for nothing.

*Then why?*

Everything was shrouded in questions.

Ailao Mountain’s Wraith had appeared out of nowhere and still hadn’t shown itself. Five Thousand-Year Spiders had suddenly begun a massacre. And there was the question of whether they were connected to Dark Heaven.

I had been frowning in thought for some time when the Beast Miao King’s voice brought me back.

“More importantly, the immediate problem is moving these people. It is a blessing that they are still breathing, but getting back out of the Poisonblood Grounds is another matter.”

I stopped thinking and answered.

“If you ask me, I think it would be better to leave the others as they are.”

“Leave them? You mean keep them here?”

“……Do I look insane to you? Of course we have to take them back to the Nanman Beast Palace. I told White Tiger to bring the people here, so it would be best to wait. Though I’m not sure he understood me properly.”

“You must mean Muyaho. He is more intelligent than most people. I am sure he understood you well enough.”

“…….”

“Why are you making that expression?”

“Oh. It’s nothing. Nothing at all.”

I almost lost it.

Muyaho. The more I heard that name, the less I could get used to it. I barely pulled my crumbling expression back together and continued.

“And I think we should leave the webs intact instead of tearing them off.”

“Because of the poison.”

“Yes.”

The journey here had been difficult, but the way back would be far worse.

We would have to make our way through the Poison Mist with more than two hundred patients who had only just awakened after spending the past several shichen in a state of full-body paralysis and unconsciousness.

*I’m not even sure how much the Myriad-Poison Ring can cover.*

The Myriad-Poison Ring certainly possessed mysterious power, but I couldn’t put two hundred lives through a fifty-fifty gacha roll just by trusting in this one item.

They were safer wrapped in the webs like this.

“At the very least, they don’t seem to be affected by the Poison Mist while they’re inside. If that weren’t the case, they would have all died on the way here.”

“That is true. The Thousand-Year Spider’s poison permeating the webs may be preventing other miscellaneous poisons from getting in.”

In a way, it was similar to using poison to suppress poison.

On the way here, the webs had been coffins.

From now on, they would be cryogenic capsules protecting their lives from the Poison Mist.

Even if I took them out one by one and detoxified them, there was a clear limit to what I could do.

At most, our conversation would go something like this.

*All right, patient. Slowly open your eyes. Can you see the fingers I’m waving in front of you? If you can, tell me how many there are.*

“Uuuh. One……one.”

*What finger is it?*

“The middle one.”

*Correct. It means fuck you.*

“Huh? What are you talking about all of a sudden……?”

*It was a simple test. Anyway, good. You can see and hear clearly now. Both your sight and hearing have recovered.*

“Thank you. Thank you so much, Han Chinese sir.”

*Ha ha. Think nothing of it. By the way, since you’ve been detoxified, your paralysis should have disappeared. Can you move your fingers?*

“Of course. I can move them just fine now.”

*Good. I have something for you to do with those fingers. But before that, may I ask your name?*

“Me? I’m Jang Sam.”

*Excellent. I’ll give you this dagger. Now write what I say on this wooden tablet.*

“Yes, yes.”

*All right. Write exactly what I say. Jang Sam.*

“Jang. Sam.”

*Lies here.*

“Lies here. Huh?”

*Actually, I didn’t tell you because I was worried you’d panic, but we have to go back the way we came. And we don’t have any poison-warding pearls left. Of course, I’m fine because I have the Myriad-Poison Ring.*

“……!”

*I’m ‘invincible.’ The Myriad-Poison Ring is a ‘god.’*

Hmm.

There was going to be a two-hundred-to-one bloodbath over the Myriad-Poison Ring.

Maybe two hundred to two. The Beast Miao King also possessed a large, beautiful, top-grade poison-warding pearl.

“……Why are you looking at me like that?”

“It’s nothing.”

“Is it Dark Heaven?”

“No. I mean heaven as in the sky.”

The Beast Miao King’s expression hardened.

“Is he really insane……?”

If my department head had been here, he would have laughed. But it seemed the Palace Lord didn’t get the joke.

The Beast Miao King looked me over with an expression like he was staring at a Thousand-Year Spider walking on two legs, then began gathering the warriors wrapped in webs into one place.

*Slice. Slice.*

Every time his straightened palm moved, the people hanging in midair were neatly stacked together.

There were two hundred of them.

Just as I had guessed, it was almost the same as the number of warriors who had disappeared from Ailao Mountain.

*Wait. What about the ferocious beasts?*

I had been helping the Beast Miao King move the survivors when I suddenly raised my head at a thought I had temporarily forgotten.

One of the questions I had had while searching Ailao Mountain in the beginning: the missing ferocious beasts were nowhere to be seen.

The Beast Miao King soon noticed it as well and wore a puzzled expression.

“That is strange. There is no sign of the ferocious beasts.”

“Could they be timid? Maybe they tuck their tails and run away when they meet people they’ve never seen before.”

“I’m asking because I’m curious, but do you perhaps not know what ‘ferocious beast’ means?”

Of course I did. Ferocious. Beast.

That was precisely why it was strange. So many ferocious beasts wouldn’t have abandoned their master and run off somewhere.

*It’s not as if the Thousand-Year Spiders are picky eaters, either.*

This was one thing I knew well. Hope Goshiwon, where I had lived for nearly seven years, had more spiders than hope.[^1]

Eventually, I had even grown fond enough of them to share my ramen.

*Then where the hell did they go?*

We would have to search the Poisonblood Grounds more thoroughly to find out, but the Thousand-Year Spiders didn’t seem meticulous enough to sort their food into separate categories.

And it was at that exact moment, while the Beast Miao King and I were looking around with puzzled expressions—

*Rustle.*

Along with a small noise, I sensed a faint presence more than ten zhang away.

[^1]: A goshiwon is a small, inexpensive room-for-rent housing arrangement, often with shared facilities.
```
