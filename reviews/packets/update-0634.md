<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0634.txt",
      "sha256": "c18cccf5f5bef02bb3ae15f64a212ab7c1b6b18b6f601896c38ade2ac5436c1e",
      "bytes": 12810
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "84594e8d6009925ed72c38a46526e43442c709ab5abf17dc6c3ff5db14d9e1d1",
      "bytes": 2681
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "bd701881777bbcee787e62c85910816d74dd6f32e48f58c9bca1b0e49d34c2ed",
      "bytes": 195076
    },
    {
      "path": "characters/Baeksang.md",
      "sha256": "9784118dd116b31f59c9233f7df5f10e0690dee89dccd2f1a9215b809f8f5338",
      "bytes": 808
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "a2f9fabce813beb44586c744f7548eec4c490178cec0c1c8695f83c53a40b5ea",
      "bytes": 553
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "f83e446e2869e40528545d0859d4bec9bc10b68001fadcc9fcbd3327ce0108d8",
      "bytes": 1702
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "ecf6b273109b7892f88c463ff1ff72ed507c43730a0a720a5c6a7c28b9af5717",
      "bytes": 201674
    }
  ],
  "estimated_tokens": 9566
}
-->

# Durable State Update — Chapter 634

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 634. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 634. Profile updates may replace only one
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
  "chapter": 634,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 634,
    "continuity_sources": [634],
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
    "The Fire Dragon Pavilion remains in temporary lodging within the Nanman Beast Palace.",
    "Nanman's first tribal council opposed joining the Murim Alliance; the second council, involving all thirty-two tribes, is tomorrow, though the Ailao Mountain crisis may disrupt it.",
    "Jin Taekyung is in Nanman to contain a spreading crisis and assess whether Nanman can be persuaded to join the Murim Alliance.",
    "Jin's tiger mask has been privately identified by Yohi and recognized by Baeksang.",
    "Baeksang is the great chieftain of the Bai people, opposes Nanman joining the Murim Alliance, and bears a burn scar from Jeok Cheongang.",
    "The Miao, Bai, Yi, and Yao peoples are Nanman's four great tribes; Yohi seeks Yao dominance while Heugung remains easily manipulated.",
    "Jin has confirmed through Qi Sense that Yohi is fundamentally different from the Southern Heaven Demon Empress.",
    "The Fire Dragon Pavilion found no trace of Dark Heaven during its investigation of the Nanman Beast Palace, but betrayal remains possible.",
    "Yayul Cheok and Baeksang were lifelong childhood friends and sworn brothers, but their present trust remains under scrutiny.",
    "Jin is certain that the Southern Heaven Demon Empress will not leave Nanman alone.",
    "Jin accepted the sudden quest Unknown Omen and is racing with Yayul Cheok to investigate Ailao Mountain within five hours.",
    "Yayul Mok has taken the Seven Miao Tigers to mobilize Miao defenses, while Namho has returned to warn the Fire Dragon Pavilion; White Tiger is temporarily carrying Jin."
  ],
  "continuity_sources": [
    633,
    632
  ],
  "open_questions": [
    "What promise did Yohi and Baeksang make, and what does Yohi intend to gain from it?",
    "Why does Baeksang believe Yayul Cheok's judgment was wrong, and can Jin change his position on the alliance?",
    "Is Baeksang's rage at Jin's mention of someone's son connected to Jin Baekyang?",
    "Will Nanman's tribal council agree to join the Murim Alliance, and is one of its thirty-two chiefs a Dark Heaven traitor?",
    "What caused the catastrophe at Ailao Mountain, what role does Dark Heaven play, and what will Jin find there?"
  ],
  "safe_through": 633,
  "temporary_decisions": [
    "Use Baeksang for 백상 and do not treat White Elephant as a separate alias.",
    "Use sworn younger brother for 불알 동생 in the relationship between Yayul Cheok and Baeksang.",
    "Render 초절정 초입 as the early stage of Supreme Peak.",
    "Render 칠묘호 as Seven Miao Tigers.",
    "Render 소족장 and 소궁주 as Young Chieftain and Young Palace Lord."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 적천강    | **Jeok Cheongang** |
| 암천     | **Dark Heaven**                  |
| 남만야수궁  | **Nanman Beast Palace**          |
| 일류     | **First Rate**    |
| 절정     | **Peak**          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 중원     | **Central Plains**                               |                                                       |
| 상태               | **Status**                     |
| 백상 | **Baeksang** | Great chieftain of the Bai people and Yayul Cheok's sworn younger brother. |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 평화 | **Peace Guild** | Guild name. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 중독 | **Poisoned** | System status abnormality caused by the poisons. |
| 남만 | **Nanman** | Historical regional term used for the source of the imported ebony. |
| 준이 | **Jun** | Family nickname used in the form Jun's dad. |
| 홍길동 | **Hong Gil-dong** | Legendary Korean outlaw invoked in Taekyung's joke about the Divine Physician. |
| 무형지독 | **Formless Ultimate Poison** | Unidentified poison discovered inside Jeok Cheongang's body. |
| 오독문 | **Five Poisons Sect** | Formerly dominant Nanman faction destroyed by the Fire Gate Clan. |
| 야수묘왕 | **Beast Miao King** | Leader of the Miao people and master of the Nanman Beast Palace. |
| 화기 | **fire qi** | The fire nature imparted to internal energy by the Fire Gate Divine Technique. |
| 전도 | **complete map of the realm** | Mae Jonghak's map marking terrain, place names, and sect locations. |
| 독물 | **venomous beasts** | Venomous creatures associated with the Nanman Beast Palace. |
| 제시 | **Jesse** | The U.S. Secretary of State, introduced by first name. |
| 애뇌산 | **Ailao Mountain** | Mountain crossed by the party on the route to the Nanman Beast Palace. |
| 백호 | **White Tiger** | Yayul Mok's tiger companion. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 야수묘왕 | 백상 | sworn_older_brother_to_sworn_younger_brother | Baeksang | familiar and bittersweet | Yayul Cheok offers Baeksang his preferred fruit wine and asks why he came. |

## Listed compact profiles

### Baeksang.md

# Baeksang (백상)

- **Safe through:** Chapter 632
- **Aliases:** None
- **Role:** Baeksang is the middle-aged great chieftain of the Bai people, one of Nanman's four most powerful great tribes.
- **Personality:** Cold, rigid, meticulous, and politically resolute, with a deep but guarded attachment to his sworn elder brother.
- **Voice:** Rigid, formal, restrained, and emotionally distant.
- **Relationships:** Baeksang is Yayul Cheok's sworn younger brother and childhood companion and Yayul Mok's sworn uncle; he lost a beloved son in the Great Faction War, bears a burn scar from Jeok Cheongang after calling him a crazy old man, opposes the Nanman Beast Palace joining the Murim Alliance, and helps Yohi keep Heugung under control.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 633
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 633
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the current Sect Leader of the Fire Gate Clan, a legendary wandering martial master who has achieved Five Qi Returning to Origin, Furnace Fire Pure Blue, and Returned to Youth, Jin Taekyung's Master who has broken free of his Heart Demon and entered a new realm, and the occupant of the chief seat of the Murim Alliance's Five Kings Hall.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, casually threatening or violent when dissatisfied, pathologically afraid of water, and more deeply trusting of Taekyung than anyone else despite responding to his impossible claims with mockery and violence.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

## Korean source

```text
＃634화



파파팟!

야수묘왕도, 백호도 걸음을 늦추지 않았다. 나는 전신을 스쳐 지나가는 스산한 바람에 눈을 가늘게 떴다.

‘저곳이 애뇌산.’

멀리서도 알아볼 수 있을 만큼 험악한 산세와 깊은 계곡. 안개에 휩싸인 수많은 봉우리는 하늘을 찌를 듯이 높다.

아직 채 가시지 않은 새벽녘의 어둠 때문일까. 아니라면 먼 과거 남만을 공포로 몰아넣었다던 오독문의 옛 본거지였기 때문일까. 빠르게 가까워지는 애뇌산의 전경은 어둡고 불길하게 느껴졌다.

아마 그런 이유에서였을 것이다. 뒤이어 들려온 야수묘왕의 목소리가 깊게 가라앉아 있는 것은.

“오독문은 본 궁에 의하여 멸문당했으나, 그렇다고 모든 것이 사라진 것은 아니었지.”

사람이 사라진 자리에 물건이 남아 있다면, 시원하게 불태워 버리면 그만이다. 하지만 그 물건에 발이 달렸다면 이야기가 달랐다.

“당시에는 누구도 몰랐다. 애뇌산 가장 깊숙한 곳에서 오독문이 남긴 알 수 없는 것들이 살아가고 있다는 것을.”

장장 백여 년.

오독문이 남긴 어두운 유산은 애뇌산 깊숙이 스며들어 살아갔다. 누구도 침범하지 못하는 자신들만의 영역에서 서로를 잡아먹고, 한편으로는 번식하며 서서히 크기를 불려 나갔다.

“하지만 결국 선조들은 알게 되었지. 누구도 바라지 않았던 방식으로.”

남만의 정예 전사 삼백이 한 줌 혈수(血水)로 녹아내렸고, 두 명의 대족장과 십여 명의 부족장이 사지가 찢겨 죽었다고 했다.

그것이 남만야수궁이 오독문을 멸문시킨 지 꼭 백 년이 되는 해에, 애뇌산에서 열린 부족 대회의에서 벌어진 일이었다.

“기록에 의하면 본 궁을 습격한 것은 남만. 아니, 천하에서도 드문 독물(毒物)과 괴이한 맹수들이었다.”

해독 방법을 알 수 없는 극독, 그리고 강철보다 단단한 발톱과 이빨을 지닌 수백 마리의 맹수.

그 누구도 예상치 못했던 습격에 극심한 피해를 입은 남만야수궁은 경악했다. 이미 오래전 사라졌다고 생각했던 오독문의 그림자를 발견하고 치를 떨었다.

“다시 한번 남만 전체가 힘을 모았다. 각 부족의 모든 전사를 동원하여 애뇌산을 포위하고 놈들을 죽이고자 했지.”

하지만 남만야수궁의 시도는 절반의 성공에 그쳤다.

수백에 달하는 맹수를 죽이고, 독물을 불태웠으나 그 손해가 너무나도 막심했던 탓이었다. 그리고 그 과정에서 보이지 않는 균열이 조금씩 생겨났다.

‘생각해 보면 그럴 수밖에 없지.’

단순히 피자 하나를 시켜서 나눠 먹더라도, 누군가는 토핑 하나라도 더 먹고 누군가는 덜 먹을 수밖에 없다.

남만야수궁의 애뇌산 토벌 작전도 비슷한 맥락이었다.

위험을 느낀 독물과 맹수들은 홍길동에 빙의된 것처럼 곳곳에서 나타나 습격을 벌였고, 전사들을 이끄는 부족장들은 자신들의 손해를 두려워했다.

막말로 이렇게 된 거, 각 부족 당 몇 명만 죽읍시다, 하고 N빵을 제시할 수도 없는 노릇이었다.

“부족은 날이 갈수록 분열되었다. 마지막 수단으로 택한 화계(火計)는 외부로 번져 더 많은 피해를 낳았을 뿐, 애뇌산 전체를 태우기에는 역부족이었고.”

그렇게 남만야수궁은 애뇌산에서 물러나야 했다. 물론 그렇다고 해서 아무런 소득 없이 물러난 것만은 아니었다.

“본 궁은 분명 극심한 피해를 입었으나 그만큼 위협도 줄어들었다. 수많은 독물과 맹수를 사냥하고 애뇌산을 일부나마 불태웠으니, 어쩌면 당연한 결과였겠지.”

“그럼 그 이후로는 어떻게 됐습니까?”

“애뇌산은 언제 그랬냐는 듯 잠잠해졌지만, 이번에는 그 누구도 방심하지 않았다. 산 전체를 금지로 지정하여 각 부족에서 차출된 정예 전사 삼백을 애뇌산에 상시 주둔시키고, 매해 네 명의 대족장이 돌아가며 소규모 토벌을 벌였지. 우리는 그런 방식으로 지난 백여 년간 평화를 유지했다.”

큰 손해를 피하면서 애뇌산의 위협을 예비할 수 있는, 남만야수궁에 속한 부족장들에게는 나름대로 현명한 타협안인 셈이다.

하지만 문제는…….

“아무래도 그 평화가, 오늘부로 마지막인 것 같네요.”

나는 잔뜩 가라앉은 목소리로 말하며 전방을 가리켰다.

내 손가락이 향하는 방향 끝에는, 지옥의 입구처럼 어둡고 험한 골짜기와 나무에 기대어 앉아 있는 한 인영이 있었다.

쉬쉬쉭!

빛살처럼 쭉 솟구친 야수묘왕의 신형이 허공을 가로질러 골짜기 입구에 내려앉는다.

그의 뒤를 바짝 쫓아 도착한 내가 백호의 등에서 내렸을 때, 인영 앞에 우뚝 선 야수묘왕의 얼굴은 석상처럼 딱딱하게 굳어 있었다.

“……늦었다. 이미 죽었어.”

나는 조용히 고개를 끄덕였다. 아마 그의 말을 듣지 않았더라도 알 수 있었을 것이다. 몇 걸음 앞까지 오기도 전에 말로는 형용할 수 없는 악취가 코를 찔렀으니까.

그리고 이토록 지독한 냄새를 풍길 만한 사인(死因)은 하나밖에 없었다.

‘독. 독이군.’

그것도 엄청난 극독이다. 나무에 기대어 고개를 숙이고 있는 인영…… 아니, 시신으로부터 흘러나온 악취와 핏물에 잠긴 땅과 풀이 까맣게 죽어 있었다.

독과 상성인 화기(火氣)를 근원으로 한 열양지기를 익히지 않은 무림인이라면, 설령 절정 초입의 고수라 해도 반경 삼 장 이내의 독기(毒氣)를 쉽게 이기지 못할 것 같았다.

- 크르릉.

나는 한껏 미간을 찡그린 백호를 다독이며 입을 열었다.

“아는 얼굴입니까?”

“왠지 모르게 낯이 익다. 필시 애뇌산에 주둔하고 있던 전사 중 한 사람이겠지.”

“원래 입구에 보초를 세워 두는 편입니까?”

“그럴 리가. 애뇌산에서 만일의 사태를 대비하기 위해서는 한 사람의 손도 아쉽다. 산이 차지하는 범위가 워낙 넓은 탓에 인근에도 마을이 서너 개가 있긴 하나, 그들도 이러한 사실을 잘 알고 있지.”

요컨대 오래전부터 엄격히 통제되던 구역이기에, 다른 보초병이 필요 없다는 뜻이다. 그리고 그렇다는 것은…….

‘이 사람은 산 위에서 내려온 거야. 무언가를 피해 도망치면서.’

나는 고개를 들어 주위를 살폈다.

짙은 어둠 너머, 흐릿하지만 분명한 족적이 남아 있었다. 한눈에 보기에도 확실히 사람의 족적이다. 짐승이나, 어떤 독물의 흔적도 보이지 않는다.

그리고 하나 더.

“상흔이 있다. 시신의 옆구리를 보아라.”

야수묘왕의 말처럼, 시신의 옆구리는 무언가가 할퀸 듯 옷이 찢겨 나갔고 피부가 온통 검게 물들어 있었다.

“우선 병장기는 아닙니다. 거칠고 강한 무언가에 단순히 스친 것 같은데…….”

“그래서 독이 무서운 것이다. 약간의 상처만으로도 삽시간에 죽음에 이를 수 있으니까.”

살짝 긁힌 것뿐인데 이 정도라니. 과거 적천강이 당했던 무형지독(無形至毒)이라도 된다는 건가?

시신에서 눈을 뗀 나는 어둠에 물든 골짜기를 응시했다. 직접 보지는 않았으나 머릿속에서 어떤 장면이 스쳐 지나가는 듯했다.

아마 저 이름 모를 망자는 조금 전까지만 하더라도 이 험한 골짜기를 내달리고 있었을 것이다. 극독에 당한 상태로 넘어지고 비틀거리며, 혼비백산하여 달려오다가 저 나무 아래에서 죽음을 맞이했겠지.

안타까운 일이지만, 지금의 내게는 저자를 죽음에 이르게 만든 것의 정체가 더욱 중요했다.

‘암천인지, 아니면 애뇌산의 독물인지. 그것도 아니면…….’

암천에 의해 조종당하는 애뇌산의 독물인지.

아직은 풀리지 않은 의문과 함께, 나는 야수묘왕을 바라보았다.

“결국 답은 하나밖에 없는 것 같은데요.”

“그래.”

야수묘왕이 분노한 맹수처럼 으르렁거리는 목소리로 말을 이었다.

“어느 놈의 소행인지, 이 눈으로 똑똑히 봐야겠다.”

띠링.



제한 시간 안에 애뇌산 조사(미완료)

남은 시간 : 01:24:32



* * *



이제 분명 어스름한 새벽이어야 할 시간임에도 애뇌산은 여전히 짙은 어둠에 잠겨 있었다.

아니, 이곳에 존재하는 것은 비단 어둠뿐만이 아니었다.

‘혈향(血香).’

어느 순간 익숙해져 버린 피비린내는 보이지 않는 길잡이였다. 죽은 이가 남긴 족적을 따라 산속을 질주하던 나와 야수묘왕은, 습한 바람을 타고 전해지는 혈향을 쫓아 망설임 없이 방향을 틀었다.

그리고 마침내 발견할 수 있었다.

산등성이 곳곳에 쓰러진 수많은 시신과, 짙은 혈향마저 덮어 버리는 극독 특유의 악취를.

“……!”

“……!”

그 숫자가 얼마나 될까. 백 명? 아니면 그 이상?

처음 골짜기에서 시신을 맞닥뜨렸을 때 떠올렸던 불길한 예상이 현실로 변했다.

눈 앞에 펼쳐진 참혹한 광경에 야수묘왕의 두 눈에서 불길이 솟구쳤다.

“어떤 찢어 죽일 놈이 감히……!”

남만야수궁의 주인인 그로서는 당연한 반응이었다. 하지만 나는 그와 함께 분노하는 대신, 최대한 침착하게 공력을 끌어올려 기막(氣幕)으로 혹시 새어 나갈지 모를 소리를 차단하고 시신들을 살폈다.

‘골절. 타박. 절단. 중독.’

처음과 달리 이곳에 쓰러진 이들의 사인은 중독 외에도 다양했다. 사지가 으스러져 절명한 이도 있었고, 알 수 없는 강한 힘에 의해 목 등의 일부가 뜯겨 나간 이들도 적지 않았다.

‘애뇌산에 주둔시킬 정도의 정예라면, 분명 상당한 실력의 소유자들.’

그런 자들이 이렇게 처참하게 당했다니.

지금까지 파악한 바에 의하면 야수묘왕과 백상을 비롯한 극소수의 인물들이 특출할 뿐, 대부분의 남만 전사들은 중원에 비해 수준이 떨어진다.

하지만 그 부분을 감안하더라도 정예 전사라면 최소 일류에서 초일류. 혹은 드물게 존재하는 절정 고수들이다.

‘게다가 남만의 전사들은 혼자 싸우지 않아. 이들과 함께하는 맹수들까지 생각한다면 중원의 명문 대파와 버금갈 전력일 텐…….’

생각을 이어 가던 나는, 문득 엄습하는 위화감에 멈칫했다. 그리고 낮은 울음소리를 흘리며 주위를 경계하는 백호를 본 순간 위화감의 정체를 깨달았다.

‘맹수. 맹수들은 어디로 간 거지?’

언제나 전사와 한 몸처럼 붙어 있는 맹수들. 그 녀석들이 보이지 않는다.

황급히 주위를 둘러보아도 마찬가지다. 얼핏 보아도 백여 구가 넘는 시신들 사이로 보이는 맹수의 사체는 서너 마리가 고작이었다.

“도대체 어째서?”

내가 마음속에 자리 잡은 의문을 입 밖으로 토해 낸 그 순간.

스아아.

“……!”

바람을 타고 전해지는, 송곳처럼 파고드는 소름 끼치는 기운.

혼란스러워하던 나도, 끓어오르는 분노를 간신히 가라앉히고 있던 야수묘왕도 번개처럼 고개를 돌렸다.

동시에 볼 수 있었다. 들을 수 있었다.

파스슥.

저 멀리, 미세하게 흔들리는 풀숲을. 살아 있는 무언가처럼 일렁이는 어둠을. 그리고…….

- 크르륵.

어둠이 내려앉은 풀숲 사이에 웅크린 어떤 존재의, 심연과도 같은 낮은 울음소리를.

사박.

느려진 세상 속, 풀숲을 짓밟으며 어둠이 움직인다.

암흑을 전신에 두른 채 우리를 향해 다가오는 그것은 지금까지 내가 본 어떤 맹수보다 거대했고, 청백색의 눈동자에는 숨길 수 없는 분노와 위엄이 서려 있었다.

‘흑호(黑虎).’

번개처럼 뇌리를 스친 한 단어와 함께, 백호의 몸뚱어리가 파르르 떨린 그 순간.

크와아아아앙!

어둠을 찢고 천지를 떨어 울리는 포효와 동시에, 낯익은 종소리가 귓가를 파고들었다.

띠링.



- [애뇌산의 망령(亡靈)]이 나타났습니다!
```

## Final English reading copy

```markdown
# Chapter 634

*Papat!*

Neither the Beast Miao King nor White Tiger slowed their pace. I narrowed my eyes against the chilly wind brushing past my entire body.

*That must be Ailao Mountain.*

Its rugged terrain and deep valleys were unmistakable even from a distance. Countless peaks shrouded in mist rose so high they seemed to pierce the heavens.

Perhaps it was because the predawn darkness had not yet lifted. Or perhaps it was because this had once been the old headquarters of the Five Poisons Sect, which had plunged Nanman into terror long ago.

Whatever the reason, Ailao Mountain’s rapidly approaching landscape felt dark and ominous.

That was probably why the Beast Miao King’s voice, which reached me soon after, had sunk so low.

“The Five Poisons Sect was destroyed by the Palace, but that did not mean everything disappeared.”

If objects remained where people had vanished, you could simply burn them away. But things were different if those objects had legs.

“No one knew at the time that the unknown things left behind by the Five Poisons Sect were still living in the deepest reaches of Ailao Mountain.”

For more than a hundred years.

The Five Poisons Sect’s dark legacy had seeped deep into Ailao Mountain and continued to live there. In a territory of their own that no one could invade, they devoured one another while breeding and slowly growing in number.

“But eventually, our ancestors found out. In a way no one had wanted.”

Three hundred elite warriors of Nanman melted into a handful of bloody water, and two great chieftains and around a dozen tribal chiefs were torn limb from limb.

That was what happened during the tribal council held at Ailao Mountain in the exact year that marked one hundred years since the Nanman Beast Palace had destroyed the Five Poisons Sect.

“According to the records, what attacked the Palace were venomous beasts and strange ferocious beasts rarely seen in Nanman—or even anywhere in the world.”

Deadly poison for which no antidote was known, along with hundreds of beasts possessing claws and teeth harder than steel.

The Nanman Beast Palace suffered enormous losses in the unexpected attack and was horrified. They trembled when they discovered the shadow of the Five Poisons Sect, which they had believed had disappeared long ago.

“Once again, all of Nanman gathered its strength. We mobilized every warrior from every tribe, surrounded Ailao Mountain, and tried to kill them all.”

But the Nanman Beast Palace’s attempt ended in only half a success.

They killed hundreds of beasts and burned the venomous creatures, but the losses they suffered were simply too great. And in the process, invisible cracks began to appear.

*When you think about it, it couldn’t have gone any other way.*

Even if you ordered a single pizza and shared it, someone would inevitably eat one extra topping while someone else got less.

The Nanman Beast Palace’s campaign to subdue Ailao Mountain had followed a similar pattern.

The venomous beasts and ferocious beasts, sensing danger, appeared and attacked from all directions as though possessed by Hong Gil-dong.[^1] The tribal chiefs leading the warriors feared the losses their own people would suffer.

[^1]: Hong Gil-dong is a legendary Korean outlaw hero proverbially said to appear here, there, and everywhere.

To put it bluntly, they couldn’t exactly say, “Since things have come to this, let’s have only a few people die from each tribe and split the bill evenly.”

“The tribes grew more divided with each passing day. As a last resort, we chose to use fire, but the flames spread outward and caused even more damage. They still weren’t enough to burn down all of Ailao Mountain.”

And so, the Nanman Beast Palace had to withdraw from Ailao Mountain. Of course, that did not mean they left with nothing to show for it.

“The Palace had suffered immense losses, but the threat had been reduced by just as much. We had hunted countless venomous beasts and ferocious beasts and burned at least part of Ailao Mountain. In that sense, perhaps the result was inevitable.”

“What happened after that?”

“Ailao Mountain grew quiet, as though nothing had ever happened, but no one let down their guard this time. We designated the entire mountain as a forbidden zone, permanently stationed three hundred elite warriors drawn from the various tribes there, and had the four great chieftains take turns leading small-scale exterminations every year. We maintained peace that way for more than a hundred years.”

It was a reasonably wise compromise for the tribal chiefs belonging to the Nanman Beast Palace—one that allowed them to guard against the threat of Ailao Mountain without suffering enormous losses.

But the problem was…

“I guess that peace is coming to an end today.”

I spoke in a heavily subdued voice and pointed ahead.

Ahead lay a dark, rugged valley like the entrance to Hell, with a lone figure sitting against a tree.

*Whoosh!*

The Beast Miao King’s body shot upward like a beam of light, crossed the air, and landed at the mouth of the valley.

When I arrived close behind him and climbed down from White Tiger’s back, the Beast Miao King stood tall before the figure. His face was stiff as stone.

“…We’re too late. He’s already dead.”

I quietly nodded. Even if I hadn’t heard him say it, I probably would have known. Before we had even come within a few steps, an indescribable stench had stabbed into my nose.

And there was only one cause of death capable of producing a smell this horrible.

*Poison. It’s poison.*

And an incredibly potent one at that. The figure leaning against the tree—no, the corpse—had released a stench and bloody runoff so strong that the ground and grass soaked in it had turned black and died.

Unless a martial artist had cultivated Scorching Yang Qi, which was rooted in fire qi and naturally opposed poison, even a master in the early stage of Peak would probably have difficulty resisting the poisonous qi within three zhang.

*Grrr.*

I soothed White Tiger, who was frowning fiercely, then opened my mouth.

“Do you recognize him?”

“Somehow, he looks familiar. He must be one of the warriors stationed at Ailao Mountain.”

“Do you normally post guards at the entrance?”

“Of course not. When preparing for an emergency at Ailao Mountain, we need every warrior we can get. The mountain covers such a vast area that there are three or four villages nearby, but even they know the situation well.”

In other words, the area had been strictly controlled for a long time, so there was no need for another sentry.

And if that was the case…

*He came down from the mountain. He was running away from something.*

I raised my head and surveyed the surroundings.

Beyond the thick darkness, faint but unmistakable footprints remained. They were clearly human footprints at a glance. There was no trace of a beast or any venomous creature.

And one more thing.

“There’s a wound. Look at the corpse’s side.”

Just as the Beast Miao King had said, the clothing along the corpse’s side had been torn as though something had clawed it, and the skin beneath had been stained completely black.

“It wasn’t a weapon, at least. It looks as though he was simply grazed by something rough and powerful, but…”

“That is why poison is frightening. Even a slight wound can bring death in an instant.”

It was only a shallow scratch, and yet this had happened.

*Could it be something like the Formless Ultimate Poison Jeok Cheongang once suffered from?*

I took my eyes off the corpse and stared into the valley drowned in darkness. I had not witnessed it myself, but a scene seemed to flash through my mind.

Until just moments ago, the unknown dead man had probably been running through this rugged valley. Poisoned, stumbling and staggering, he had fled in a panic before meeting his death beneath that tree.

It was tragic, but the identity of whatever had killed him was more important to me right now.

*Was it Dark Heaven, or one of Ailao Mountain’s venomous beasts? Or else…*

One of Ailao Mountain’s venomous beasts being controlled by Dark Heaven.

With the question still unanswered, I looked at the Beast Miao King.

“In the end, it seems there’s only one answer.”

“That’s right.”

The Beast Miao King continued in a growling voice like an enraged beast.

“We’ll have to see with our own eyes exactly which bastard did this.”

*Ding.*

> **System**
>
> **Investigate Ailao Mountain Within the Time Limit (Incomplete)**
>
> **Time Remaining:** 01:24:32

* * *

Even though it should have been the dim hour of dawn by now, Ailao Mountain remained shrouded in thick darkness.

No. Darkness was not the only thing that existed here.

*The scent of blood.*

The smell of blood, which had become familiar at some point, was an invisible guide. Following the footprints left behind by the dead man, the Beast Miao King and I raced through the mountain before turning without hesitation toward the scent of blood carried on the damp wind.

And at last, we found it.

Countless corpses collapsed across the mountain ridges, along with the distinctive stench of deadly poison that even overwhelmed the heavy scent of blood.

“……!”

“……!”

How many were there? A hundred? Or more?

The ominous prediction I had made when we first encountered the corpse in the valley had become reality.

At the horrific sight spread before him, flames rose in the Beast Miao King’s eyes.

“Which bastard dared…? I’ll tear him limb from limb!”

It was a natural reaction from the ruler of the Nanman Beast Palace. But instead of joining him in his anger, I calmly drew up my internal energy, formed a qi curtain to block any sounds that might escape, and examined the corpses.

*Fractures. Blunt-force trauma. Dismemberment. Poisoning.*

Unlike the first corpse, the deaths here had varied causes besides poisoning. Some had died with their limbs crushed, while many others had parts of their bodies—their necks and elsewhere—torn away by some unknown, overwhelming force.

*If they were elite enough to be stationed at Ailao Mountain, they must have possessed considerable skill.*

And yet they had been slaughtered this horribly.

From what I had learned so far, only a very small number of Nanman’s warriors—including the Beast Miao King and Baeksang—were exceptional. Most of Nanman’s warriors were inferior to those of the Central Plains.

But even taking that into account, elite warriors would have been First Rate at minimum, reaching Transcendent or, in rare cases, Peak masters.

*Besides, Nanman’s warriors don’t fight alone. If you consider the ferocious beasts fighting alongside them, their combined strength should rival that of the major sects of the Central Plains…*

I was continuing that thought when I suddenly stopped at the strange feeling creeping over me. The moment I saw White Tiger keeping watch over the surroundings with a low growl, I realized what had caused it.

*The beasts. Where did the beasts go?*

The beasts that were always attached to their warriors as though they were one body were nowhere to be seen.

I hurriedly looked around, but it was the same everywhere. Among the more than a hundred corpses visible at a glance, there were only three or four beast carcasses.

“Why on earth?”

The instant I voiced the question that had taken root in my mind—

*Hsssss.*

“……!”

A chilling energy came riding the wind, piercing into me like an awl.

I had been confused, while the Beast Miao King had been barely suppressing his boiling rage. But both of us turned our heads like lightning.

At the same time, we saw it. We heard it.

*Rustle.*

Far away, grass trembled faintly. Darkness undulated as though it were alive. And then—

*Grrr.*

A low growl, deep as an abyss, came from some creature crouched among the grass where darkness had settled.

*Step.*

In a world that seemed to have slowed, the darkness moved, trampling the grass.

Wrapped in darkness from head to toe, it came toward us. It was larger than any beast I had ever seen, and its blue-white eyes held unmistakable anger and dignity.

*Black Tiger.*

The word flashed through my mind like lightning. At that exact moment, White Tiger’s body began to tremble.

*Gwaaaaaaaaaang!*

As a roar tore through the darkness and made heaven and earth tremble, a familiar ringing tone pierced my ears.

*Ding.*

> **System**
>
> - **Ailao Mountain’s Wraith** has appeared!
```
