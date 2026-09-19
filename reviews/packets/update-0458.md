<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0458.txt",
      "sha256": "41dfa20a590e7bae9a06df7edb3017a92cccfa67846a6d763ce461d4a5873a88",
      "bytes": 13414
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "184e7d85842b21ec670f8fed0608e8ec3aa1b535a8c9095d8c9122f6a1f6f0f3",
      "bytes": 3802
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "0b998337c839105c5077ef69def81a57db4e8ea50973089fde2af471f041acfd",
      "bytes": 149724
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "e8a1c48710fc5eed1665aad1ec13bb4c814bf38da97d247382666d3808eab7ec",
      "bytes": 944
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "05cb094e72c86d237f68d9f635baa09b7e86a1728d163f24aadfe1faca5d60b7",
      "bytes": 553
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "e4b00187d918331395a2449be6f0b84d8c345747b0317cc435c2bee1e8edb52c",
      "bytes": 662
    },
    {
      "path": "characters/Honglan.md",
      "sha256": "69028301d95870b9c10f3c7d05a6e2467c2d270f38de1a72089c1afba64fd022",
      "bytes": 605
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "fb86e3db24aeba6401dad84d2c4b21cb4129c20a8dadfb017ab741bd6b01a217",
      "bytes": 1108
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "7dde30348656c0c1ea70150e405af08f80e062c0c592d1d4725732fe8c15bf73",
      "bytes": 1477
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "1d7107a8fccbd7f22fc575f87ee5c27e0f5f94254f8deee40b1e0f78feb0b44d",
      "bytes": 144359
    }
  ],
  "estimated_tokens": 10829
}
-->

# Durable State Update — Chapter 458

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 458. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 458. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history.
`names` contains only newly required Korean-to-English rows that are absent from
Exact glossary matches; Korean keys must occur in the source. Do not repeat
glossary matches. The controller drops rows already in the names ledger.
`address_pairs` contains only newly required speaker→addressee rows that are
absent from Matched address pairs. Speaker and addressee must be Hangul source
spellings such as 진태경 or 혁무진, never English names. Arabic digits are
allowed in titles such as 1팀장. At least one endpoint must occur in the source.
The controller drops pairs already in the address ledger. Do not invent
risk-register rows. Beat plot paragraphs are plain strings; continuity and
translation decisions are concise list items.
Return this exact shape:

{
  "chapter": 458,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 458,
    "continuity_sources": [458],
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
    "Taekyung accepted Quest Another Chaos to uncover the truth behind the Hubei incidents and find the culprit.",
    "Jin Wikyung is acting as an inspector for the new Murim Alliance and is cooperating with Taekyung's investigation.",
    "The shared symbols between the Arch Lich's magic circle and Dark Heaven's formations remain unexplained.",
    "The Sea Serpent Society and three Yangtze River Channel League strongholds, including Donghu Stronghold, were destroyed, with more than a thousand casualties, while the perpetrators' whereabouts remain unknown.",
    "The Dongting Fisherman is believed to remain in Hubei Province and is suspected of being a Dark Heaven member involved in the Hubei atrocities.",
    "Wudang is responding to an unidentified killer demon responsible for more than thirty deaths, including twenty pilgrims on Mount Wudang.",
    "The Skeleton King's undead identity remains concealed, and Taekyung has ordered him to join Peace Guild under a prepared contract.",
    "Go Jun is expected to succeed Lee Jungryong as Ares Guild's captain and is searching China for Lee's holographic recorder.",
    "The unavoidable Peak-grade Quest The Tragedy of Dongting Lake is active at Dongting Lake; all nearby victims were dead, Qi Sense found no survivor within range, Taekyung split the search with Cheongpung and Gung Gibang while Hyuk Mujin gathered boats and people, and a distant survivor has just called for help.",
    "The captured Three Fiends is a former-generation great fiend and Supreme Peak Dark Heaven subordinate whom Taekyung is transporting alive to investigate possible codes or markings.",
    "Qingxia Hall is an influential Hubei social club formed by powerful families' children, and Ju Wongong is its exiled young master who defers to Prince Shangshan while Honglan conceals her real name.",
    "Beggars' Sect, Lower District Sect, and Zhuge Clan intelligence are searching for the people responsible for the Hubei massacres."
  ],
  "continuity_sources": [
    457,
    456
  ],
  "open_questions": [
    "What are the origin and purpose of the symbols shared by the Arch Lich's magic circle and Dark Heaven's formations?",
    "Who destroyed Donghu Stronghold and the related Yangtze River Channel League strongholds, why was no Moving Formation trace left, and was the destruction a diversion?",
    "Is the Dongting Fisherman a member of Dark Heaven, what role did he play in the Hubei atrocities, who sank the boat in Dongting Lake, and who is the distant survivor now calling for help?",
    "Is the killer demon attacking Wudang connected to Dark Heaven?",
    "What evidence is contained in Lee Jungryong's holographic recorder, and what are the terms of the Peace Guild–Wizard Guild agreement?"
  ],
  "safe_through": 457,
  "temporary_decisions": [
    "Render 익양루 as Yiyang Tower.",
    "Render 황철 as Hwang Cheol, 도립군 as Do Ripgun, 광수도귀 as Mad Water Saber Demon, 파랑호 as Wave Fox, 동정호 as Dongting Lake, and 사천혈사 as Sichuan Blood Tragedy.",
    "Render 살귀 as killer demon, 일급 낭인 as First Rate wandering martial artist, 삼괴 as Three Fiends, 대마두 as great fiend, and 마군 as Demon Lord.",
    "Render 시부럴 as “sibu-leol,” 시벌좌 as “Lord Fuck,” and 시부럴좌 as “Lord Sibu-leol.”",
    "Preserve the Skeleton King's grandiose, mock-offended voice and Taekyung's dry, profane humor; render 주원공 as Ju Wongong, 대죽산표국 as Daejuksan Escort Bureau, 형문검가 as Hyungmun Sword Family, 응성상회 as Eungseong Merchant Association, 천룡인 as Celestial Dragon, 사인교 as four-person sedan chair, 홍란 as Honglan, 가기 as singing courtesan, and 구족 as the nine branches of kin."
  ],
  "version": 1
}
```

## Exact glossary matches

| 혁무진    | **Hyuk Mujin**     |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 제갈세가   | **Zhuge Clan**                   |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 곰방대   | **long-stemmed tobacco pipe**                    |                                                       |
| 은인     | **Benefactor**                               |
| 시스템              | **System**                     |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 홍란 | **Honglan** | Stage name of Ju Wongong's Lower District Sect singing courtesan; her real name is concealed. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 천년독각사 | **Thousand-Year Poison Horned Snake** | Extremely venomous horned snake used to make Hong Dao's thirty-year-old liquor. |
| 일각 | **fifteen minutes** | Quarter of a shichen; used for the remaining completion time. |
| 아귀 | **A-Gwi** | Legendary Dogon from Sichuan. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 미미 | **Mimi** | Worker at Honghwaru referenced in Taekyung's joke. |
| 미미쨩 | **Mimi-chan** | Affectionate form used for Tang Mimi. |
| 동정채 | **Donghu Stronghold** | Stronghold where Mu Song's Uncle Hwang is based. |
| 동정호 | **Dongting Lake** | Lake under which Dangyang and Honghu Strongholds operated. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 청풍 | 미미 | handler_to_companion_snake | Mimi | cheerful-commanding | Cheongpung repeatedly calls and commands the Thousand-Year Poison Horned Snake. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 457
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 455
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** Publicly reputed to be selfless and devoted to treating patients in the lowest places.
- **Voice:** Not established.
- **Relationships:** Mungyeong is the Divine Physician's true identity, and Dong Feng is his Disciple.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 457
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung and uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and search for Dark Heaven’s Hubei forces.

### Honglan.md

# Honglan (홍란)

- **Safe through:** Chapter 454
- **Aliases:** None
- **Role:** Honglan is a Lower District Sect courtesan who uses a stage name while serving as Ju Wongong's singing courtesan.
- **Personality:** Discreet about her real identity and professionally alluring.
- **Voice:** Clear, pure, and alluring, with humble formal speech toward honored guests.
- **Relationships:** She is kept at Ju Wongong's side as a singing courtesan, belongs to the Lower District Sect, and can respond to Taekyung through Sound Transmission.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 457
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 436
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather; more than forty years ago he sought Jeok Cheongang's help against the Demonic Cult, fought Jeok at Mount Jiuhua for seven days and seven nights, and drew with him; after the Great Faction War ended, he devoted himself to martial arts, reached Great Completion, attained higher enlightenment after encountering another wall, unexpectedly Returned to Youth, and traveled the world for a year under the name Jongni Chu while concealing his identity; at Mount Song he protected Cheongpung and attacked the Blood Lord with the divine Thirty-Six Plum Blossom Swords; after the Blood Lord escaped, he confirmed his identity to Jin Taekyung and Song Ho, and Song Ho identified Mae as the Great Hero who had saved his life.
- **Personality:** Not established in this chapter.
- **Voice:** Not established in this chapter.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

## Korean source

```text
＃458화



‘사, 살려 주…….’



꺼져 가는 불씨처럼, 아주 작고 희미한 목소리.

하지만 그것만으로도 충분했다. 아무도 구하지 못했다는 무력감에 젖어 있던 가슴이 거세게 뛰고, 풀어졌던 전신에 힘이 샘솟는다.

나는 소리가 들려온 방향을 따라 몸을 날렸다.

‘인벤토리 오픈, 소환!’

퉁!

이제 얼마 남지 않은 나룻배의 파편이 강물에 비친 달을 쓸었다.

새처럼 허공 위로 도약한 나는 얼마 남지 않은 공력을 끌어 올려 눈에 집중했다.

극도로 향상된 안력(眼力)이 발아래 펼쳐진 광경을 일목요연하게 받아들인다.

‘저건…….’

선박의 잔해와 시신.

비록 산산이 분해되어 원래의 형체를 알아볼 수 없게 되었지만, 지금까지 동정호에서 본 것 중 가장 크고 화려한 선박이었으리라는 건 의심의 여지가 없었다.

‘저 중 어딘가에 생존자가 있다.’

문제는 당장 보이는 시신의 숫자와 잔해가 너무 많다는 것이었다.

하지만 머뭇거릴 틈 따위는 없었다.



제한 시간 : 59초



59초. 고작 일 분도 되지 않는 이 짧은 시간에 생존자의 목숨이 달렸다.

나는 눈을 감고 호흡을 가다듬었다. 어느새 바닥을 드러내고 있는 공력을 있는 힘껏 끌어 올렸다.

솨아아아악!

기감(氣感).

전신으로부터 뻗어 나간 청백색 열양지기가 넘실거리는 강물 위를 내달린다.

이미 혼이 떠나간 백여 구의 시신과 무수히 많은 선박의 잔해를 샅샅이 훑고 뒤졌다.

그리고 마침내.

“……!”

보였다. 아니, 느껴졌다.

수십 장 너머, 지금도 시시각각 수면 아래로 가라앉고 있는 미약한 기운이.

나는 감았던 눈을 반개(半開)했다.



제한 시간 : 32초



신체 내부를 순환하던 열양지기가 하반신을 향해 치닫는다.

공력이 집중된 발끝으로 허공을 밟자, 압축된 공기가 터져 나가는 소리와 함께 찬바람이 전신을 타고 흘렀다.

퍼엉! 쐐애애애액!

나는 유성처럼 쏘아졌다. 바람이 갈라지고 공간이 지워졌다.

양옆으로 주위의 풍경이 휙휙 스쳐 지나갔지만, 시선은 오직 한 곳에 고정되어 있었다.

거칠게 출렁이는 검은 강물. 저 안에 생존자가 있다.

‘빌어먹을, 수영도 못 하는데.’

문득 그 생각이 뇌리를 스친 순간, 동정호의 강물이 내 전신을 후려쳤다.

촤악! 푸그르르르!

숨이 턱 막힐 정도의 충격.

무공을 익히지 않았다면 뼈가 부러지고 오장육부가 진탕되었을 것이다.

나는 물거품을 뿜으며 수면 아래로 가라앉았다.

갑작스러운 불청객의 등장에 화들짝 놀란 물고기 떼가 흩어지자, 천천히 가라앉고 있던 두 개의 인영이 보였다.



제한 시간 : 20초



‘더, 더, 더……!’

나는 젖먹던 힘까지 끌어 올려 나아갔다. 이미 의식을 잃고 축 늘어진 두 사람의 손목을 틀어쥐고 힘차게 위로 솟구쳤다.

10초. 9초, 8초…….

수면 위에 비친 희미한 달빛이 가까워진다.

팔과 다리가 철구를 매단 것처럼 무겁고 양손에 잡힌 두 사람이 천근거석처럼 느껴졌다. 그리고 다음 순간.

촤악!

“푸하아!”

참았던 숨을 토해 냈다.

시릴 정도로 차가운 공기가 폐부 깊숙이 스며들었다.

하지만 생존자들을 물 밖으로 끌어냈다고 해서, 모든 게 끝난 것은 아니었다.



제한 시간 : 3초



그 순간, 나는 본능적으로 내가 해야 할 일을 깨달았다.

‘살린다.’

오직 그 일념 하나가 잠시 멈춰 있던 몸뚱어리를 움직였다.

나는 미약한 공력이 실린 쌍장(雙掌)을, 두 사람을 향해 내뻗었다.

펑!

몸이 들썩이고 물이 튄다.

그러나 아무런 반응도 보이지 않는 생존자들 대신, 허공에 떠오른 시스템 창의 숫자가 바뀌었다.



제한 시간 : 2초



‘한 번 더……!’

펑!



제한 시간 : 1초



모든 시간이 느려졌다.

1이라는 얄팍한 숫자 하나가 그 어느 때보다 거대하고 육중하게 나를 짓누른다.

멍하니 시스템 창을 바라보며 눈을 부릅뜬 바로 그 순간이었다.

“푸읍.”

“콜록, 콜록.”

간절히 기다리던 생존자들의 호흡이 돌아옴과 동시에, 마지막 숫자로 변화하려던 시스템 창이 정지했다.

그리고 축포와도 같은 종소리가 울려 퍼졌다.

띠링.



- [인명 구조]에 성공했습니다!

- 돌발 퀘스트, [동정호의 비극]을 완료했습니다!

- 당신은 퀘스트를 성공적으로 완료했습니다. 그에 합당한 보상이 주어집니다!

- 상당량의 경험치와 명성을 획득했습니다!

- 칭호, [수상 구조대원]을 획득했습니다!



나는 귓가를 파고드는 알림을 들으며 중얼거렸다.

“시부럴.”

결국 해냈다는 기쁨과 안도감은 둘째치고, 제갈세가에서부터 시작된 강행군으로 지쳐 있던 몸이 천근만근 무겁다.

어쩌면 아슬아슬하게 유지되던 긴장감이 탁 풀렸기 때문일지도 모르겠다.

‘……빌어먹을. 이거 다시 육지로 가려면 한참인데.’

이러다가 나까지 구조받아야 하는 거 아니냐.

두 생존자와 함께 몸의 부력을 이용해 둥둥 떠 있던 그때였다.

촤아아아악!

저 멀리에서 제트 스키처럼 빠르게 물살을 가르며 다가온 ‘그것’이 내 앞에서 멈췄다.

새하얀 몸통과 비늘, 그리고 두 개의 뿔.

“물뱀……이 아니라, 천년독각사?”

췻. 췻. 취췻!

안 돼, 어디 가!

나는 혀를 날름거리고 몸을 돌리려는 녀석을 향해 황급히 외쳤다.

“야! 야! 물뱀! 천년독각사!”

췻!

“너 이 새끼 지금 나한테 침 뱉은 거…… 아니, 잠깐만.”

이거 설마 삐쳤다는 표현인가?

문득 머릿속에 떠오른 한 가지 생각에, 나는 간절하면서도 조심스러운 목소리로 입을 열었다.

“미미, 미미쨩?”

취릭! 취리릭!

그제야 흡족하게 고개를 끄덕인 천년독각사, 아니 미미쨩이 내게 마치 붙잡으라는 듯 자신의 꼬리를 내민다.

때맞춰 저 멀리에서 누군가의 외침이 들려왔다.

“미미! 은인 구하기!”

취릭!

“…….”

그래, 시벌. 기술명이야 아무래도 상관없으니까 어서 나 좀 데려가라.



* * *



나는 축축한 바위에 앉아 넘실거리는 강물을 바라보았다.

두 명. 단 두 명이다.

오늘 동정호에 뼈를 묻은 수많은 사람 중, 내가 구한 두 사람만이 유일한 생존자였다.

‘……그 많은 사람 중에서 고작 둘이라니.’

퀘스트가 완료되었을 때부터 짐작하고 있던 사실이지만, 현실은 내가 생각했던 것 이상으로 잔인하고 냉혹했다.

그리고 오늘의 참극이 남긴 무수한 죽음은 그 이상의 슬픔을 낳았다.

“허어…….”

“크흑, 크흐흑!”

“아이고, 칠삼이 아부지!”

“어, 어느 천인공노할 놈이 이런 짓을!”

동정호의 강가에는 어느새 천여 명으로 불어난 사람들이 갖가지 감정을 쏟아내고 있었다.

차마 말을 잇지 못하고 탄식하는 유생. 동료의 시신을 붙잡고 눈물을 흘리는 관병의 뒤에는 갓난아이를 등에 업은 아낙네의 통곡이 뒤따른다. 나이 지긋한 노인은 목에 핏대를 세운 채 보이지 않는 누군가에게 곰방대를 휘두르기도 했다.

천하에서 손꼽히는 명승지인 동정호에는 더 이상 웃음이나 노랫소리를 찾아볼 수 없었다.

남겨진 자들의 슬픔과 탄식, 그리고 그 모든 감정이 실린 분노만이 있을 뿐.

하지만 바뀌는 것은 없다. 동정호의 강물은 언제 그랬냐는 듯 잠잠해졌고, 어스름하게 내리깔린 새벽 안개는 아름다운 풍경을 자아냈다.

신선들이 산다는 무릉도원(武陵桃源)이 이런 모습일까?

눈앞에 펼쳐진 광경을 말없이 바라보던 나는 불쑥 입을 열었다.

“기분 참, 뭐 같네. 안 그래?”

혼잣말이 아니다.

일각이 넘도록 곁을 떠나지 않고 있던 청풍이 대답했다.

“네, 좆 같아요.”

평소 같았으면 참지 못하고 실소를 흘렸을 텐데, 지금은 그저 공허하다.

나는 조약돌을 만지작거리며 물었다.

“그냥 뭐 같다고만 했는데. 청 소협이 그런 욕도 할 줄 알았어?”

“처음에는 몰랐는데, 이젠 그럭저럭 알아요. 어떤 사람을 보면서 배웠거든요.”

“그거, 매종학 대협한테는 비밀로 하는 게 좋겠는데.”

“왜요, 은인?”

“왜냐니. 미미가 어느 날 갑자기 청 소협한테 씨발 놈이라고 하면 어떤 기분일 것 같아?”

“으음. 별로일 것 같아요.”

“……보통은 뱀이 말하면 놀라는 게 먼저 아닌가. 어쨌건 놀라기도 하고, 화도 나겠지. 매종학 대협도 마찬가지고.”

“아아. 그렇구나.”

“그래, 그런 거지.”

“혹시 할아버지 앞에서 실수로 욕이 나오면 어떡하죠?”

“궁기방이 가르쳐 줬다고 해. 아니면 혁무진이나.”

“네에.”

침묵이 흘렀다.

조금 전의 대화는 그저 나오는 대로 끄집어낸 헛소리들에 불과하다. 무슨 말이라도 해야 할 것 같아서. 이렇게라도 하면 조금은 나아질까 싶어서.

나도, 청풍도 그 사실을 안다.

이렇게 한다고 해서 지금의 감정이 나아지지 않으리라는 것 역시도.

“시발…….”

나는 한탄처럼 욕설을 중얼거렸다.

오늘이 유난스러운 날인지, 아니면 저 녀석들도 사정을 알고 슬퍼하는지.

새들의 울음소리는 들리지 않았고 다만 사람들의 통곡과 흐느낌만이 주위에 가득했다.

그 먹먹하면서도 참을 수 없는 소리들을 가만히 듣다가, 손바닥 위에 올려둔 조약돌을 힘껏 움켜쥐었다.

콰득, 파스슥.

한 줌이나 될 법한 가루가 손아귀에서 흘러내린다. 아니, 어디선가 불어온 바람에 실려 강물 위로 사뿐히 내려앉는다.

마치 누군가의 넋이 서린 유골이라도 되는 것처럼.

그 광경을 말없이 지켜보던 청풍이 문득 입을 열었다.

“은인.”

“왜?”

“이럴 땐 어떻게 해야 하죠?”

“…….”

“너무 많은 사람들이 죽었어요. 하남에서, 사천에서, 그리고 동정채와 바로 오늘, 이곳에서.”

이어지는 목소리가 가늘게 떨렸다.

“죽은 이들의 모습이 자꾸만 생각나요. 그리고 화가 나요. 자꾸만 사람들을 죽이는 그들이 밉고, 아무것도 못 하는 저 자신이 한심스러워요.”

“……나도 그랬지. 아니, 지금도 그래.”

“이럴 때마다 은인은 어떻게 했어요?”

“나?”

고개를 돌리자, 비로소 청풍과 마주할 수 있었다.

티 하나 없이 맑던 눈동자에는 여러 감정이 뒤섞여 휘몰아치고 있었다.

그 혼란한 감정 속에서 과거의 내가, 그리고 지금 청풍을 응시하고 있는 현재의 내가 보인다.

‘이런 모습이었나.’

청풍의 눈을 통해 바라본 현재의 내 모습은…… 그저 덤덤했다.

궁기방이나 혁무진처럼 지쳐 있지도 않았고, 가족과 동료를 잃은 사람들만큼 분노와 슬픔으로 몸을 떨지도 않았다.

아니, 감정을 느끼지 못하는 것이 아니라 갈무리한 것이다.

오랜 세월 무언가에 끊임없이 부딪쳐 닳고 깎여 나가, 마침내는 익숙해져 버린 바위가 바로 그곳에 있었다.

“글쎄. 내가 어떻게 했더라.”

잠시 생각하던 나는 천천히 말을 이었다.

“청 소협이랑 다를 거 없어. 그 쳐죽일 놈들을 향해 쉴 새 없이 욕하고, 내 무능함을 자책하고, 마지막으로 다짐하지.”

“다짐, 이요?”

“응. 다짐.”

나는 손가락을 들어 슬픔에 잠긴 사람들과 강가에 놓인 시신들을 가리켰다.

“이런 짓을 벌인 놈들을 반드시 죽여 버리겠다. 그런 다짐.”

“……!”

“나는 성인군자가 아니라서, 최소한 받은 만큼 돌려줘야 직성이 풀리더라고. 이번에도 마찬가지고.”

남의 것처럼 낯선, 건조하면서도 차가운 목소리가 입술을 비집고 흘러나온 바로 그 순간이었다.

“조장님.”

피로한 기색이 역력한 혁무진이 다가와 말했다.

“생존자들이 정신을 차렸습니다.”

“그거 잘됐네. 둘 다?”

“아뇨. 우선 한 사람뿐입니다.”

안타깝긴 하지만, 내심 짐작하고 있던 일이었다. 구조 후 내가 취한 조치는 긴급 처방일 뿐이었으니까.

“그래, 가자.”

“예. 이리로.”

나와 청풍은 혁무진을 따라 걸음을 옮겼다. 그리고 비로소 정신을 차린 생존자 중 한 사람과 마주할 수 있었다.

“금방 다시 만났네. 그렇죠?”

내가 건넨 인사에 눈부신 미모의 가기, 홍란(紅蘭)이 지극히 공손한 태도로 예를 취했다.

“은인을 뵙습니다.”
```

## Final English reading copy

```markdown
# Chapter 458

*P-please, save me…*

Like a dying ember, the voice was tiny and faint.

But that alone was enough. My heart, weighed down by the helplessness of having failed to save anyone, began pounding fiercely, and strength surged through my limp body.

I launched myself in the direction of the voice.

*Inventory: Open. Summon!*

*Thud!*

A remaining fragment of the ferry skimmed across the moon’s reflection on the water.

I leaped through the air like a bird, drew up the last of my internal energy, and focused it in my eyes.

My drastically enhanced vision took in the scene below with perfect clarity.

*That’s…*

Shipwreckage and corpses.

Though the vessel had been smashed into pieces beyond recognition, there was no doubt that it had been the largest and most splendid ship I had seen on Dongting Lake.

*There’s a survivor somewhere among them.*

The problem was that there were far too many corpses and fragments visible at once.

But there was no time to hesitate.

> **System**
>
> **Time Limit:** 59 seconds

Fifty-nine seconds. The survivor’s life depended on the brief span of less than a minute.

I closed my eyes and steadied my breathing. Then I drew up every last bit of my internal energy, which was already nearly depleted.

*Fwoooooosh!*

Qi Sense.

The Scorching Yang Qi extending from my entire body raced across the rippling water.

It swept through the more than one hundred corpses whose souls had already departed, as well as the countless fragments of ships, searching every inch.

And finally—

“……!”

I saw it.

No—I felt it.

Dozens of zhang away,[^1] a faint qi that was even now sinking beneath the surface by the second.

I opened my eyes halfway.

> **System**
>
> **Time Limit:** 32 seconds

The Scorching Yang Qi circulating through my body rushed toward my lower half.

When I stepped on empty air with the tips of my toes, the compressed air exploded outward, and a cold wind swept across my entire body.

*Boom! Fwoooooosh!*

I shot forward like a meteor. The wind split apart, and space seemed to vanish.

The scenery on either side flashed past, but my gaze remained fixed on a single point.

The rough, surging black water.

There was a survivor in there.

*Damn it. I can’t even swim.*

The thought had barely crossed my mind when Dongting Lake slammed into my entire body.

*Splash! Gurgle!*

The impact was enough to make my breath catch.

If I had not learned martial arts, my bones would have broken and my internal organs would have been shaken to pieces.

I sank beneath the surface, exhaling a cloud of bubbles.

A school of fish scattered in alarm at the sudden arrival of an unwelcome visitor, revealing two figures slowly sinking into the depths.

> **System**
>
> **Time Limit:** 20 seconds

*More. More. More…*

I summoned every last bit of strength I had and pushed forward. I seized the wrists of the two unconscious, limp figures and surged upward with all my might.

Ten seconds. Nine, eight…

The faint moonlight reflected on the surface drew closer.

My arms and legs felt as heavy as if iron balls had been tied to them, while the two people in my hands weighed like thousand-catty boulders.

And then—

*Splash!*

“Puaaah!”

I expelled the breath I had been holding.

Air cold enough to sting flowed deep into my lungs.

But pulling the survivors out of the water did not mean everything was over.

> **System**
>
> **Time Limit:** 3 seconds

In that moment, I instinctively realized what I had to do.

*Save them.*

That single thought moved my body, which had briefly come to a stop.

I thrust both palms, infused with what little internal energy I had left, toward the two people.

*Boom!*

Their bodies jerked, and water splashed.

But instead of any response from the unresponsive survivors, the number on the System window floating in the air changed.

> **System**
>
> **Time Limit:** 2 seconds

*One more time…*

*Boom!*

> **System**
>
> **Time Limit:** 1 second

Everything slowed down.

That paltry digit of 1 grew larger and heavier than ever, pressing down on me.

I was staring blankly at the System window, my eyes wide, when—

“Puh.”

“Cough, cough.”

At the same moment the survivors’ breathing finally returned, the System window, which had been about to change to its final digit, stopped.

Then a bell rang out like a victory cannon.

*Ding.*

> **System**
>
> - You succeeded in **Rescuing Lives**!
> - You completed the unexpected Quest **The Tragedy of Dongting Lake**!
> - You have successfully completed the Quest. An appropriate Reward will be granted!
> - You acquired a considerable amount of EXP and Fame!
> - You acquired the Title **Water Rescue Worker**!

I listened to the notification drilling into my ears and muttered,

“Sibu-leol.”

The joy and relief of having finally succeeded came second to the crushing heaviness of my exhausted body. I had been worn down by the forced march that began at the Zhuge Clan.

Maybe it was because the tension I had maintained by a thread had suddenly snapped.

*…Damn it. It’ll take forever to get back to land.*

At this rate, would I end up needing to be rescued too?

That was when I found myself floating with the two survivors, using my body’s buoyancy.

*Whoooooosh!*

Something cut rapidly through the water in the distance like a jet ski before stopping right in front of me.

A pure-white body and scales, along with two horns.

“A water snake…? No, a Thousand-Year Poison Horned Snake?”

*Hiss. Hiss. Hiss-hiss!*

“Hey, don’t go anywhere!”

I hurriedly shouted at the creature as it flicked its tongue and turned away.

“Hey! Hey! Water snake! Thousand-Year Poison Horned Snake!”

*Hiss!*

“You little bastard, did you just spit at me—wait.”

Could this be its way of expressing that it was sulking?

One thought suddenly came to mind, and I opened my mouth in an earnest yet cautious voice.

“Mimi… Mimi-chan?”

*Hiss-rik! Hiss-ririk!*

Only then did the Thousand-Year Poison Horned Snake—or Mimi-chan—nod in satisfaction and extend its tail toward me as if telling me to hold on.

Right on cue, someone shouted from far away.

“Mimi! Rescue Benefactor!”

*Hiss-rik!*

“…….”

Yeah, fuck it. Who cared what the technique was called? Just get me out of here.

* * *

I sat on a damp rock and stared at the rippling water.

Two people. Only two.

Of all the countless people who had buried their bones in Dongting Lake today, the two I had saved were the only survivors.

*…Only two out of all those people.*

I had suspected it from the moment the Quest was completed, but reality was even more brutal and merciless than I had imagined.

And the countless deaths left behind by today’s tragedy had given rise to even greater sorrow.

“Ugh…”

“Sniff, sob!”

“Oh, poor Chil-Sam’s father!”

“What inhuman bastard could have done such a thing!”

By then, the number of people gathered along the shore of Dongting Lake had grown to more than a thousand, and they poured out every emotion imaginable.

A Confucian scholar lamented, unable to continue speaking. Behind a government soldier clutching a fallen comrade’s corpse and weeping came the wails of a woman with an infant strapped to her back. An old man, the veins standing out on his neck, even swung his long-stemmed tobacco pipe at some unseen culprit.

There was no longer any laughter or singing to be found at Dongting Lake, one of the most famous scenic sites under heaven.

Only the sorrow and lamentation of those left behind remained, along with the anger infused in all those emotions.

But nothing changed.

The waters of Dongting Lake had grown calm, as if nothing had happened, while the faint dawn mist spreading across the lake created a beautiful scene.

*Is this what the Wuling Peach Blossom Spring where immortals are said to live looks like?*[^2]

I stared silently at the scene before me, then spoke without warning.

“This feels like… something, doesn’t it?”

I was not talking to myself.

Cheongpung, who had not left my side for more than fifteen minutes, answered,

“Yes. Like fucking shit.”

Under normal circumstances, I would have snorted with laughter despite myself. But now, I felt nothing but empty.

I fidgeted with a pebble and asked,

“I only said ‘something.’ I didn’t know Young Hero Cheongpung knew how to swear.”

“I didn’t at first, but I know a little now. I learned by watching someone.”

“You’d better keep that a secret from Great Hero Mae Jonghak.”

“Why, Benefactor?”

“Why do you think? How would you feel if Mimi suddenly called you a fucking bastard one day?”

“Hmm. I don’t think I’d like it.”

“……Wouldn’t most people be surprised that a snake was talking before getting angry? Either way, you’d be surprised and angry. Great Hero Mae Jonghak would be the same.”

“Oh. I see.”

“Yeah. That’s how it is.”

“What should I do if I accidentally swear in front of Grandfather?”

“Say Gung Gibang taught you. Or Hyuk Mujin.”

“Okay.”

Silence descended.

That conversation had been nothing more than nonsense dragged out as it came to me. I had felt that I needed to say something—anything. I wondered if doing so might make things a little better.

Both Cheongpung and I knew the truth.

We also knew that doing this would not make our current feelings any better.

“Fuck…”

I muttered the curse like a lament.

I did not know whether today was simply an unusual day, or whether those creatures also understood the circumstances and were grieving.

There was no birdsong.

Only the wails and sobs of the people filled the air around us.

I listened quietly to those stifling, unbearable sounds, then clenched the pebble resting in my palm as hard as I could.

*Crack. Crunch.*

A handful of powder spilled from my fist.

No—it was carried by a breeze that had blown in from somewhere and settled lightly on the surface of the water.

As if they were mortal remains imbued with someone’s spirit.

Cheongpung watched the scene in silence before suddenly speaking.

“Benefactor.”

“What?”

“What should I do at times like this?”

“…….”

“So many people have died. In Henan, in Sichuan, at Donghu Stronghold, and today, here.”

His voice trembled faintly as he continued.

“I keep thinking about the dead. And I get angry. I hate the people who keep killing others, and I feel pathetic for being unable to do anything.”

“……I was like that too. No, I still am.”

“What did Benefactor do whenever you felt this way?”

“Me?”

I turned my head and finally met Cheongpung’s gaze.

His eyes, usually clear without a single blemish, were swirling with a mixture of emotions.

Within that confusion, I saw my past self—and the present me staring at Cheongpung now.

*Was I like this?*

The current version of myself, viewed through Cheongpung’s eyes, was simply impassive.

I was not exhausted like Gung Gibang or Hyuk Mujin, nor was my body trembling with anger and sorrow like those who had lost their families and companions.

No, it was not that I could no longer feel emotions.

I had merely learned to contain them.

The rock that had collided with something again and again over many years, worn and ground down until it had finally grown accustomed to it, stood there before me.

“Who knows? What did I do back then?”

After thinking for a moment, I slowly continued.

“I wasn’t any different from you, Young Hero Cheongpung. I swore nonstop at those bastards who deserved to die, blamed myself for my helplessness, and then made a vow.”

“A vow?”

“Yeah. A vow.”

I raised a finger and pointed at the grieving people and the corpses laid out along the shore.

“I vowed to kill every last bastard who did this. That was my vow.”

“……!”

“I’m no saint. I won’t be satisfied until I pay them back at least in equal measure. This time is no different.”

That was when a dry, cold voice that felt unfamiliar, almost as if it belonged to someone else, slipped through my lips.

“Captain.”

Hyuk Mujin approached us, exhaustion plainly visible on his face.

“The survivors have regained consciousness.”

“That’s good. Both of them?”

“No, sir. Only one of them, for now.”

It was unfortunate, but I had suspected as much. The treatment I had performed after rescuing them had only been an emergency measure.

“Then let’s go.”

“Yes, sir. This way.”

Cheongpung and I followed Hyuk Mujin.

At last, we came face-to-face with one of the survivors who had regained consciousness.

“We’ve met again rather quickly, haven’t we?”

At my greeting, Honglan, the singing courtesan of dazzling beauty, bowed with the utmost respect.

“It is an honor to see you, Benefactor.”

[^1]: A **zhang** is a traditional Chinese unit of distance, roughly 3.3 meters.

[^2]: Wuling Peach Blossom Spring is a classical Chinese image of an idyllic, isolated utopia.
```
