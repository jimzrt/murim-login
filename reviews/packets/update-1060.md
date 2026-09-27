<!-- packet-manifest
{
  "included": [
    {
      "path": "source/1060.txt",
      "sha256": "8512e3368121c0d69a46a190e8322b1e832ce8e6c1c248ea7e8c3ad1dd7e5af5",
      "bytes": 12605
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "ef1c5541f96532ff49aba7607c430e2c3fbee75d02f12a3b07ac604c2627c423",
      "bytes": 1475
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "00393f64552a324b59de22435e669f9c3775156bdb7d88fb36f641805263e183",
      "bytes": 241117
    },
    {
      "path": "characters/Divine Physician.md",
      "sha256": "5af12ad800d08b39b227e8e1d3f5a74a92c7a605189bf5da06703a4441a1c0d2",
      "bytes": 760
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "093127dd0bde968d48f7f6ffc557d9ee13340f121102bf5995a04ec98d579efc",
      "bytes": 686
    },
    {
      "path": "characters/Hyeoncheon.md",
      "sha256": "276d5f2679007d1f5a41aa682f9cb44f32d2a795c35378fc59698e4e9a0afbaf",
      "bytes": 651
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "3cb06ce9b25f2e75293b4a48cee5b32ff851126ed151e231cff9c98884187521",
      "bytes": 1375
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "2e4b3bfec8e778304925e5803c74bbdb03d05dbbbb9cdba3ccc60acafd9150ba",
      "bytes": 1502
    },
    {
      "path": "characters/Ma Junggeol.md",
      "sha256": "530a8e97905794731037b33aec673befec7409ac2d8c95cc333bb55472193764",
      "bytes": 673
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "2dfa3ce8db63f974fd931dd4d864e8f0d79ef43290fe89f407950d649e2f9c1f",
      "bytes": 282809
    }
  ],
  "estimated_tokens": 10350
}
-->

# Durable State Update — Chapter 1060

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

For each matched character, check whether this chapter adds clear, durable
evidence that improves Role, Personality, Voice, or Relationships. Update a
field when it corrects or meaningfully sharpens the existing profile; otherwise
leave it unchanged. Voice guidance should capture observable register, cadence,
word choice, or address habits that help distinguish the character in English.
Do not infer a stable voice from one situational line or generic personality
adjectives. Keep “Not established” only when this chapter provides no reliable
voice evidence; never replace it with unsupported specificity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 1060. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 1060. Profile updates may replace only one
complete line in Aliases, Role, Personality, Voice, or Relationships. Do not
return Safe through updates; the controller sets that field automatically.
Each profile field should be one concise sentence; never append semicolon-separated
chapter history. For a new profile, describe voice only when the chapter supports
a useful, stable distinction; otherwise say “Not established”.
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
  "chapter": 1060,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 1060,
    "continuity_sources": [1060],
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
    "Hyeoncheon spared Sama Pyo after wounding him shallowly; he declares that the Kongtong Sect will pursue revenge without punishing relatives for their kinship.",
    "Taishan charged toward Sama Pyo, and Taekyung stopped him by knocking him unconscious.",
    "Hyeoncheon tells the surviving Kongtong Disciples to grieve for their dead.",
    "Some Kongtong Sect survivors vanished to an unknown location.",
    "The Lord of Heaven’s identity and connection to Asmodeus remain unknown.",
    "The Grand Mage departed for Qinghai on a new mission; the identity of the other servant remains unknown.",
    "A mysterious green light remains in the dispersing darkness.",
    "Jeok Cheongang and the Bow Saint returned with an unidentified, foul-smelling man whom Jeok called a madman; some mounted bandits call him Great Sir."
  ],
  "continuity_sources": [
    1058,
    1059
  ],
  "open_questions": [
    "What are the identity and purpose of the Lord of Heaven, and is he connected to Asmodeus?",
    "Where did the missing Kongtong Sect survivors go?",
    "What is the new mission in Qinghai, and who is the other servant there?",
    "What is the mysterious green light?",
    "Who is the foul-smelling man, and why do some mounted bandits call him Great Sir?"
  ],
  "safe_through": 1059,
  "temporary_decisions": [
    "Render 대인 as “Great Sir” for the mounted bandits’ address to the unidentified man."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 궁성     | **Bow Saint**                 | —              |
| 일신     | **One God**         |
| 암천     | **Dark Heaven**                  |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 중원     | **Central Plains**                               |                                                       |
| 마적     | **mounted bandits**                              |                                                       |
| 장문인    | **Sect Leader**                              |
| 제자     | **Disciple**                                 |
| 스킬               | **Skill**                      |
| 게이트     | **Gate**              |
| 감숙     | **Gansu**              |
| 청해     | **Qinghai**            |
| 정마대전   | **Great Faction War**         |
| 본문      | **our sect / this sect**                                        |
| 신의 | **Divine Physician** | Sobriquet of the legendary anonymous physician sought to treat Jeok Cheongang. |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 현천진인 | **Perfected Being Hyeoncheon** | Current Sect Leader of Wudang and Hyeongong's Senior Brother. |
| 마중걸 | **Ma Junggeol** |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 인내 | **Endurance** | System attribute replacing Toughness. |
| 후개 | **Successor Beggar** | Title of the Beggars' Sect successor competing in the preliminaries. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 청해성 | **Qinghai** | Source form specifying Qinghai as a province. |
| 근력 | **Strength** | System attribute increased by Jin Taekyung. |
| 인천 | **Incheon** | Location of the airport welcome and presidential greeting. |
| 공동파 | **Kongtong Sect** | Sect belonging to the Nine Sects and One Gang. |
| 마방 | **horse caravans** | Descendants of northern mounted tribes who traveled ancient trade routes between the Outer Lands and the Central Plains. |
| 서울 | **Seoul** | Location announced for the World Hunter Federation's inaugural ceremony. |
| 녕하성 | **Ningxia Province** | Region between Gansu and Shaanxi. |
| 백마방 | **Baekma Bang** | Ma Junggeol’s horse-caravan group, founded by reformed mounted-bandit leaders. |
| 백마칠종 | **Seven Masters of Baekma Bang** | Collective title for Ma Junggeol and his six associates. |
| 돈황 | **Dunhuang** | City identified as the foremost defensive line in Gansu. |
| 진인 | **Perfected One** | Honorific for the two Kongtong Elders killed at Dunhuang. |
| 녕하 | **Ningxia** | Place name; origin of the mounted bandits mentioned by Sima Gong. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 적천강 | 신의 | senior_martial_master_to_physician | Divine Physician | blunt and familiar | Uses 신의 while recognizing Dong Feng’s medical identity. |
| 신의 | 적천강 | physician_to_legendary_martial_master | Sir Jeok | formal-deferential | Uses 적 대협 while thanking and counseling Jeok. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 적천강 | 궁기방 | overwhelming_elder_to_younger_martial_artist | you | blunt and threatening | Jeok Cheongang rebukes Gung Gibang for speaking informally and orders him to lie down. |
| 적천강 | 궁성 | old acquaintance and fellow martial master | you; nasty old hag | blunt and familiar | Uses a contemptuous insult while expressing concern for his Disciple. |
| 궁성 | 적천강 | old acquaintance and fellow martial master | you | familiar and lightly teasing | Speaks with dry familiarity about his unchanged, impulsive nature. |
| 마중걸 | 적천강 | visiting horse-caravan chief to legendary martial master | Great Hero Jeok Cheongang | polite and deferential | Recognizes Jeok as the Fire King. |

## Listed compact profiles

### Divine Physician.md

# Divine Physician (신의)

- **Safe through:** Chapter 1059
- **Aliases:** Medicine Immortal
- **Role:** The Divine Physician is Mungyeong, the legendary physician and former Slaughter Saint who passed the Divine Physician title to his Disciple.
- **Personality:** He is devoted to medicine and the lives he could not save, yet remains composed and self-effacing under mortal danger.
- **Voice:** He speaks in calm, respectful, self-effacing language, framing mortality through quiet philosophical reflections.
- **Relationships:** Mungyeong is the Divine Physician's true identity, the Slaughter Saint was his Master, and Dong Feng is his Disciple.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 852
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Gung Gibang is a rival finalist alongside Baek Woo and Zhuge Gyun who trades insults with Taekyung, uses Beggars’ Sect intelligence to investigate Tang Taesang’s murder and Dark Heaven’s Hubei forces, and has now found a trace of Honglan.

### Hyeoncheon.md

# Perfected Being Hyeoncheon (현천진인)

- **Safe through:** Chapter 1059
- **Aliases:** None
- **Role:** Perfected Being Hyeoncheon is the current Sect Leader of the Kongtong Sect, a veteran Daoist master, and a Supreme Peak martial artist.
- **Personality:** Grave and reflective, he bears the losses of the Great Faction War yet rejects punishing the innocent for their relatives’ crimes.
- **Voice:** Measured, solemn, and calm with the authority of a Sect Leader.
- **Relationships:** Hyeongong is his Junior Brother, and both studied under the same master from childhood.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 1056
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers, Vice Squad Leader of the Jin Dragon Squad, and an active member of the Fire Dragon Pavilion.
- **Personality:** Young, disciplined, persistent, and talented; despite being naturally fearful, he faces danger and remains loyal to the person he serves, with irreverent self-deprecation and a taste for glory. He is suspicious of Taekyung, bluntly critical of the family's disgraced third son, and an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; with Taekyung, blunt and occasionally incredulous, while using breezy, irreverent banter to defuse tense situations.
- **Relationships:** He is loyal to Taekyung, who trusts him to act independently, especially in his home region of Shanxi and at the Jin Family of Taiyuan. As a former family gate guard, he knows the most about Head Elder Jin Baekyang among the Fire Dragon Pavilion members accompanying Taekyung. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 1059
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is the Fire Gate Clan’s current Sect Leader, a legendary martial master who has surpassed the Three Saints, Jin Taekyung’s Master and intended heir’s mentor, and a trusted confidant who occupies the chief seat of the Murim Alliance’s Five Kings Hall.
- **Personality:** Secretive, sharp-eyed, gruff, dryly teasing, and pathologically afraid of water; he distrusts process-first excuses when outcomes fail and hopes to make good choices while protecting those he still has.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** He considers Jin Taekyung his one and only Disciple and trusted confidant, and insists on protecting Taekyung while urging him not to risk his life; he warmly regards Ju Hwaran, sees Mae Jonghak as a kindred spirit, recognizes Cheongpung as Mae's grandson and successor, was close to Hong Dao, accepted Jangcheon as a Disciple before he became Jopil, and was Peng Cheolhu’s longtime rival and friend until Peng’s death, when they parted reconciled as brothers in all but blood; he once fought alongside Murong Baek, now his enemy, and personally killed his former ally the Junzi Saber after that man joined the Demonic Cult.

### Ma Junggeol.md

# Ma Junggeol (마중걸)

- **Safe through:** Chapter 1056
- **Aliases:** Chief of Baekma Bang
- **Role:** Ma Junggeol is the chief of Baekma Bang, a horse-caravan group founded by reformed Ningxia mounted-bandit leaders.
- **Personality:** Though timid by nature, he is earnest and protective of his sworn brothers, loyal to the benefactor who helped them reform, and willing to bear personal risk for their mission.
- **Voice:** Not established
- **Relationships:** He leads six sworn brothers who, with him, are known as the Seven Masters of Baekma Bang, and trusts the benefactor they call the Lord.

## Korean source

```text
1060화




대인(大人).

이름도, 신상도 알려진 바 없는 정체불명의 초절정 고수.

지금으로부터 약 십여 년 전, 무법천지나 다름없던 녕하성(寧夏省)을 단숨에 평정한 뒤 모두의 예상을 뒤엎고 날백수로 전직했다는 희대의 기인이사를 처음 마주한 내 감상은 이랬다.

‘거지 같은데.’

단순한 비유가 아니라, 실제로 그랬다.

얼굴을 덮는 것으로도 모자라 허리춤에 닿을 정도로 길게 자란, 심지어 잔뜩 떡 져 있는 머리카락과 수염.

군데군데 찢어지고 얼룩이 가득한 의복은 차라리 누더기라고 부르는 것이 옳았고, 땟국물이 줄줄 흐르는 몸에서 풍기는 냄새는 혁신적이다 못해 혁명적이었다.

그야말로 거지 중의 거지.

상거지. 혹은 왕초 거지.

명실상부한 십만 떼거지의 소두목, 개방의 후개(後丐)인 궁기방조차 이 양반을 마주한다면 구걸 좆같이 하네를 외치며 허리춤에 묶은 밧줄을 끊으리라 장담할 수 있었다.

그런데…….

“정말 이 사람이 말로만 듣던 그 거지, 아니 대인이라고요?”

“믿을 수 없게도, 모두 사실이다.”

이미 멀찍이 떨어진 채 코를 틀어막고 있던 궁성이 코맹맹이 소리로 대답한 그때였다.

“아이고오오오! 대이이인! 왜 이제 오셨습니까아아!”

애달픈 외침과 함께 저 멀리에서 후다닥 달려온 백마칠종의 맏형, 마중걸이 괴인을 와락 끌어안았다.

아니, 정확히는 끌어안으려다가 불에 덴 듯이 화들짝 놀라며 허리를 새우처럼 굽혔다.

“우욱, 웩.”

“…….”

그래, 충분히 이해한다.

나만 해도 게이트에서 굴러먹다 온 짬바가 있어서 이렇게 버티고 있는 거지, 지금도 이게 진짜 사람 몸에서 나는 냄새인가 싶을 정도니까.

물론, 그런 나조차도 슬슬 한계에 봉착하고 있었다.

“잠깐, 잠깐만 좀 떨어져 봐요. 이거 초면에 왜 이래.”

처음의 당황스러운 마음도 잠시.

나는 필사적인 구강 호흡으로 냄새를 최대한 차단하며 괴인을 밀어 냈지만, 천근 바위처럼 지면 깊게 틀어박힌 그의 두 다리는 꿈쩍도 하지 않았다.

‘이런 거 보면 진짜 대인이 맞는 것 같은데…….’

아무리 나 스스로 힘을 조절했다고는 하나, 일반적인 한계를 아득히 벗어난 근력은 어지간한 절정 고수도 버틸 수 없다.

하지만 머릿속과 달리 가슴은 이해를 못 한다.

서울역 2번 출구를 주름잡는 노숙자 김씨가 알고 보니 대기업 회장이었다더라, 뭐 그런 느낌이라고 해야 하나.

‘아니, 근데 뭐 이렇게 서럽게 울어.’

어찌해야 할지 모르는 상황 속에서 내가 눈동자만 굴리던 그때, 내 품에서 목 놓아 통곡을 이어 가던 괴인. 아니 대인이 그제야 코 먹은 목소리로 입을 열었다.

“큼. 크흐흠. 미안하네. 너무 감동적인 상황이라 나도 모르게 눈물이 흐르더군.”

나는 끈적하게 젖은 가슴팍을 내려다보며 정정해 주었다.

“눈물만 흐른 건 아닌 것 같은데요.”

“콧물도 흐르더군.”

눈물 콧물이야 나온다 치더라도 그걸 왜 내 품에 안겨서 흘리는지 모르겠지만, 나는 연장자에 대한 최소한의 예의와 인내심을 담아 고개를 끄덕였다.

“아, 예. 그래서 뭐 지금은 괜찮으시죠?”

“덕분에 조금 진정이 되는군. 잠깐 코 좀 풀어도 되겠나?”

“진짜 가지가지 하네.”

“응? 뭐라고?”

“아닙니다. 마음껏 푸세요.”

“고맙네.”

그리고 순박한 어조로 감사를 표한 대인은, 속이 뻥 뚫리는 것 같은 소리를 내며 코를 풀었다.

패애애앵!

내 옷자락에.

“후우, 시원하…… 그런데 자네 표정이 왜 그러나?”

“…….”

아.

이성이 끊긴다, 진짜로.



* * *



결론적으로 말하자면, 나는 이성이 반쯤 끊어진 상황 속에서도 용케 대인의 죽통을 후려갈기지 않았다.

아직 완전히 수습되지도 않은 전장의 한복판에서 그런 일을 벌이는 것은 현명하지 못한 짓이기도 했고, 무엇보다 빠르게 상황을 파악한 현천진인이 끼어들었기 때문이었다.

“여기 계셨습니까, 대인.”

그건 누가 보더라도 상당히, 아니 매우 놀라운 광경이었다.

현천진인이 누구인가.

바로 그 구파일방의 일익인 공동파의 장문인이자, 정마대전의 영웅 중 한 사람이며, 감숙성을 대표하는 초절정 고수다.

해병대로 치자면 인천 상륙 작전까지 참가했던 전설의 1기 참전 용사고, 천하의 한복판에서 ‘내 아래 니 위로 집합’을 외쳐도 되는 짬밥인 것이다.

한데 무림에서의 배분도, 일신에 지닌 무위도 천하에서 수위에 꼽히는 그가 극진한 예의를 갖춘 채 먼저 포권지례를 올렸다.

그것도 개방 방주도 울고 갈 만한 몰골을 한 괴인에게.

오죽했으면 그 광경을 지켜보고 있던 적천강이 이렇게 중얼거릴 정도였다.

“도대체 무슨 약점을 잡힌 거지……?”

사실 그 순간만큼은 나도 어느 정도 비슷한 생각을 떠올렸다.

상거지 꼴을 한 저 양반이 공동파 H모 진인의 은밀한 손장난, 뭐 그런 제목을 지닌 동영상 파일이라도 가지고 있나 싶어서.

그러나 현천진인이 기껏해야 전직 마적 나부랭이들이 따르는 괴인에게 정도의 예의를 갖추는 데에는, 모두가 납득 할만한 이유가 있었다.

“여기 계신 대인께는 참으로 큰 도움을 받았네.”

이야기를 정리하자면 이랬다.

당시 돈황에서 패퇴한 현천진인과 공동파의 생존자들은 어디로 향해야 할지 모르는 상황에 처해 있었다.

서쪽에서 구름처럼 몰려드는 암천의 군세를 피해 동쪽으로 도주해야 했지만, 이미 아군에 대한 배신감이 마음속에 싹 튼 이상 호랑이 아가리로 들어가는 꼴이나 다름없었으니까.

하여 택한 곳이 북쪽, 바로 북방의 초원이었다.

“곧장 남쪽으로 발길을 돌려 청해(靑海)로 향할까 생각도 해보았지만, 이미 암천이 그곳에서 무슨 일을 벌였을지 몰라 훨씬 인적이 드문 초원으로 향할 수밖에 없었지.”

비록 청해성이 중원 끝자락에 머무른 변방이라고는 해도, 지켜보는 이목이 사방에 수두룩하다.

반면 초원은 광활하고 그에 비해 인구가 적어 도주에 적합했으니, 두 곳 모두 암천의 마수가 뻗쳤다는 전제하에서는 백이면 백 후자를 택할 수밖에 없었다.

“우리는 쉬지 않고 북쪽으로 향했네. 안서(安西)를 지나 초원으로 진입한 후에도 쉬이 마음을 놓지 못했지. 잠시 심신을 추스른 뒤 감숙에서의 상황을 지켜보거나, 혹은 그대로 초원을 가로질러 섬서까지 갈 생각도 하고 있었네.”

그러나 이미 돈황에서의 격전으로 크고 작은 부상을 입은 공동파의 제자들에게 있어, 그건 결코 쉽지 않은 강행군이었다.

당장 모두를 이끌어야 할 현천진인조차 극심한 내상으로 한계에 다다라 있었으니까.

“그럼에도 멈출 수 없었지. 그저 비참하고도 막연한 심정으로 계속해서 이동할 수밖에 없었네. 한데 그렇게 꼬박 며칠을 보낸 어느 날 밤, 저 멀리서 웬 불빛이 어른거리지 뭔가.”

초원의 밤은 깊고 적막하다.

끝없이 펼쳐진 그 땅을 가로지르던 도주자들에게, 어둠 속을 밝히는 불빛은 곧 경계의 대상이나 다름없었다.

“한껏 숨죽여 다가갔는데, 웬 정체불명의 괴인이 낙타 고기를 굽고 있더군. 나흘 만에 보는 음식에 모두 정신이 혼미해졌지.”

어느샌가 가까이 다가와 집중해서 듣고 있던 혁무진이 아, 하고 낮은 탄성을 흘렸다.

“그게 저 거지, 아니 대인이십니까?”

현천진인이 고개를 끄덕였다.

“물론일세. 추위에 떨고 있던 우리를 보더니 망설임 없이 자리를 권하셨지.”

“크. 거기에 더해 먹을 것까지 기꺼이 내주시다니, 장문인께서 고마워하실 만도 합니다.”

훈훈한 미담에 주위의 공기가 한층 따뜻해진 그때, 현천진인이 입을 열었다.

“아니, 우리는 못 먹었네.”

“예?”

“우리가 보이자마자 게 눈 감추듯 고기를 해치우더니, 불이나 좀 쬐고 서로 갈 길 가자고 하시더군.”

“……!”

“……!”

뭔데 시벌.

나를 비롯한 모두의 눈길이 쏠리자, 대인이 산발을 한 머리카락을 수줍게 매만졌다.

“그때는 나 혼자 먹을 양밖에 없어서…….”

다시 차갑게 식은 공기 속, 현천진인이 말을 이었다.

“여하튼 결론적으로는 대인께서 큰 도움을 주셨지. 빈도를 비롯한 본문의 제자 모두에게 잠시 머무를 은신처를 제공하고, 부상자들도 치료해 주셨네.”

자고로 고수는 고수를 알아보는 법.

처음에는 현천진인 역시 이 정체불명의 초절정 고수를 경계했지만, 그 외의 다른 선택지는 마땅치 않았고 얼마 지나지 않아 그의 진심 어린 호의를 느끼게 되었다고 했다.

“그러던 차에 뜻하지 않은 방문도 있었지.”

“뜻하지 않은 방문이라면……?”

“처음에는 은신처의 위치를 알아낸 적들이 기습해 오는 줄 알았네. 하지만 아니었어. 들어 보니 백골칠종인가 하는 자들이 대인을 모시러 왔다더군.”

가만히 듣고 있던 마중걸이 이를 악물며 끼어들었다.

“백마칠종. 백마칠종이오.”

“아, 착각했군. 흑마칠종이었던가?”

“아니 백마칠종이라니까. 나 참 진짜 미치고 환장…….”

빡.

묻지도 따지지도 않고 마중걸의 뒤통수를 후려쳐 조용하게 만든 나는 주위를 둘러보았다.

거칠게 투레질하는 말 위에 앉아 전장 곳곳을 돌아다니는 적지 않은 수의 기마인(騎馬人)들.

비교적 가벼운 가죽 갑옷과 돌격창, 월도 등으로 무장한 그들의 정체를, 이제야 비로소 확신할 수 있었다.

“그럼 혹시 저자들이……?”

“지금 자네가 생각하는 것이 맞네. 다름 아닌 녕하성의 마방(馬房)들이지.”

오만상을 쓴 채 뒤통수를 어루만지던 마중걸이 기어가는 목소리로 끼어들었다.

“정확히는 백마방(白馬房)을 중심으로 한…… 헉!”

나와 눈이 마주치자 입을 꾹 다물었지만, 이번에는 머리를 때리는 대신 어깨를 두드려 주었다.

며칠 전 대인을 모셔오겠다며 약속하고 떠난 백마칠종이 휘하의 마방들을 이끌고 돌아온 덕분에, 무너져 가던 적들에게 결정적인 치명타를 가할 수 있었으니까.

‘이게 이렇게 되네.’

사실 그들의 존재를 반쯤은 잊고 있었다.

아니, 크게 기대하지 않았다고 하는 것이 더 옳은 표현일지도 모른다.

전투는 늘 최악의 상황을 염두에 두어야 하고, 전직 마적 출신의 마방들은 썩 신뢰할 수 있는 대상이 아니었으니까.

하지만 그들은 처음 정했던 시일보다 조금 늦었을지언정 끝내 나와 한 약속을 지켰고, 대인의 호의 아래 부상을 회복한 현천진인과 공동파의 제자들은 수천의 마방들과 함께 감숙으로 되돌아올 수 있었다.

그럼에도 단 하나, 아직도 해결되지 않는 의문이 있다면…….

‘그래서, 도대체 저 인간의 진짜 정체는 뭐지?’

나는 의문이 뒤섞인 눈빛으로 대인이라 불리는 그자를 바라보았다.

조금 전에는 이산가족 상봉이라도 한 것마냥 내 품에 안겨 통곡하더니, 이제는 조금 이야기가 길어졌다고 하품까지 쩍쩍 해 대는 그는 확실히 제정신과는 거리가 멀어 보였다.

마중걸과 그의 의형제들에게 익히 들었던 대로.

그리고 그런 대인을 향해, 나는 조용하고 은밀히 손을 뻗었다.

보이지 않는, 오직 내게만 허락된 탐지의 손을.

‘스킬, 기감 발동.’

솨아아악.

나를 중심으로 뻗어 나간 푸른 원이, 마침내 대인에게 닿았다.
```

## Final English reading copy

```markdown
# Chapter 1060

Great Sir.

An unidentified Supreme Peak master whose name and identity were unknown.

My first impression of the extraordinary man who, about a dozen years ago, subdued Ningxia Province—then little better than a lawless wasteland—in a single stroke, only to defy everyone’s expectations and retire into a life of idleness, was this:

*He looks like a damn beggar.*

That wasn’t just a figure of speech. He really did.

His hair and beard were long enough to cover his face and reach his waist, and so matted they looked like one solid mass.

His clothes were torn and stained in so many places that “rags” would have been the more accurate description. And the stench coming off his grime-caked body was so revolutionary it was practically an evolution of its own.

A beggar among beggars.

A wretch. A king of beggars.

Even Gung Gibang, the Beggars’ Sect’s Successor Beggar and a bona fide minor chief among its hundred thousand beggars, would take one look at this man and cry, “You beg like shit!” I could guarantee he’d cut the rope tied around his waist.

And yet…

“So this really is the beggar everyone’s heard about—or, I mean, the Great Sir?”

“Hard as it is to believe, it’s all true.”

The Bow Saint answered in a nasal voice. She was already standing well away, pinching her nose shut.

That was when—

“Greeeaat Siiiir! Why did you take so long to come?!”

With a plaintive wail, Ma Junggeol, eldest of the Seven Masters of Baekma Bang, came sprinting from far off and threw his arms around the strange man.

Or, more accurately, he tried to hug him, then recoiled as if burned and doubled over like a shrimp.

“Ugh. Blegh.”

“……”

Yeah, I understood.

I’d spent enough time rolling around in Gates to have built up some resistance, which was the only reason I could stand there. Even now, the stench was bad enough to make me wonder if it could really be coming from a human body.

Of course, even I was reaching my limit.

“Wait, just—give me a little space. Why are you doing this when we’ve only just met?”

My initial shock didn’t last long.

I desperately breathed through my mouth to block out as much of the smell as possible, then tried to push the man away. But his legs were planted deep in the ground like thousand-pound boulders. He didn’t budge.

*Looking at that, he really does seem like a Great Sir…*

Even though I’d held back, my strength was so far beyond ordinary limits that even a decent Peak master would have struggled to withstand it.

My head understood. My heart didn’t.

It was like hearing that Kim, the homeless guy who ran the second exit at Seoul Station, had turned out to be the chairman of a major corporation.

*But, seriously, why are you crying so hard?*

As I stood there, unsure what to do and darting my eyes around, the strange man—no, the Great Sir—who’d been wailing in my arms finally spoke in a congested voice.

“Ahem. Ahem. Sorry about that. It was such a moving moment that the tears came before I knew it.”

I looked down at the front of my chest, soaked and sticky, and corrected him.

“I don’t think tears were the only thing that came out.”

“My nose was running, too.”

I could understand tears and a runny nose, but why he had to let them both out while clinging to me was beyond me. Still, I nodded, summoning the bare minimum of patience and respect for my elder.

“Uh, sure. So you’re feeling better now?”

“Thanks to you, I’ve calmed down a little. Do you mind if I blow my nose?”

“You really do everything, don’t you?”

“Hmm? What was that?”

“Nothing. Go ahead.”

“Thank you.”

The Great Sir thanked me in a guileless voice, then blew his nose with a sound that seemed to clear out his entire head.

*Phaaaang!*

On my clothes.

“Whew, that feels much better… Why are you making that face?”

“……”

Ah.

I was really about to snap.

* * *

To sum it up, even with half my sanity gone, I somehow managed not to punch the Great Sir in the head.

Starting a fight in the middle of a battlefield that hadn’t even been fully secured yet would have been unwise. More than that, Perfected Being Hyeoncheon had quickly grasped what was happening and stepped in.

“Here you are, Great Sir.”

It was a sight that would have surprised anyone. No—astonished them.

Who was Perfected Being Hyeoncheon?

The Sect Leader of the Kongtong Sect, one of the Nine Sects and One Gang; a hero of the Great Faction War; and a Supreme Peak master representing Gansu Province.

If we were talking about the Marine Corps, he’d be a legendary first-wave veteran who’d taken part in the Incheon Landing Operation. He had the seniority to stand in the middle of the world and shout, “Everyone below me and above you, fall in!”

And yet this man, whose standing in the Murim and martial prowess both ranked among the highest in the world, was the first to offer a fist-and-palm salute with the utmost respect.

To a strange man who looked worse than even the Beggars’ Sect leader.

It was enough to make Jeok Cheongang, watching from nearby, mutter:

“What the hell does he have on him…?”

For that moment, I had more or less the same thought.

Maybe the filthy-looking fellow had a video file with a title like *Kongtong’s Perfected One H and His Secret Hand Games*.

But there was a reason everyone could understand why Perfected Being Hyeoncheon would show that much respect to a strange man followed by little more than some former mounted bandits.

“This Great Sir was of tremendous help to us.”

To sum up the story, it went like this.

At the time, Perfected Being Hyeoncheon and the Kongtong Sect survivors had been defeated at Dunhuang and had no idea where to go.

They had to flee east to avoid Dark Heaven’s forces gathering like clouds in the west. But now that they felt betrayed by their allies, heading east would have been like walking straight into a tiger’s jaws.

So they chose to go north, toward the grasslands.

“We considered turning south for Qinghai, but we had no idea what Dark Heaven might already have done there. We had no choice but to head for the grasslands, where fewer people lived.”

Though Qinghai lay at the far edge of the Central Plains, it was still watched from every direction.

The grasslands, by contrast, were vast and sparsely populated, which made them better for evading pursuit. If Dark Heaven had reached both places, anyone would have chosen the latter.

“We kept heading north without rest. Even after passing Anxi and entering the grasslands, we couldn’t let our guard down. We considered taking a short break to recover and see what was happening in Gansu, or perhaps crossing the grasslands and going all the way to Shaanxi.”

But for the Kongtong Disciples, already suffering injuries both serious and minor from the fierce battle at Dunhuang, it was an exhausting march.

Even Perfected Being Hyeoncheon, who had to lead them all, had reached his limit from severe internal injuries.

“Still, we couldn’t stop. We had no choice but to keep moving, feeling helpless and miserable. Then, after several days on the road, one night we saw a light flickering in the distance.”

The nights on the grasslands were deep and silent.

For the fugitives crossing that endless expanse, any light in the dark was something to be wary of.

“We crept closer, holding our breath. There was some strange man roasting camel meat. It had been four days since we’d seen food, and we were all half out of our minds.”

Hyuk Mujin had drifted closer at some point and was listening intently. He let out a low, “Ah.”

“Was that the beggar—sorry, the Great Sir?”

Perfected Being Hyeoncheon nodded.

“Indeed. He saw us shivering in the cold and invited us over without hesitation.”

“Now that’s generous. He even offered you food. No wonder you’re grateful, Sect Leader.”

The heartwarming story made the air around us feel a little warmer. Then Perfected Being Hyeoncheon spoke again.

“No, we didn’t get any.”

“What?”

“As soon as he saw us, he devoured all the meat before our eyes and told us we could warm ourselves by the fire for a while, then go our separate ways.”

“……!”

“……!”

What the hell?

Everyone’s eyes turned toward the Great Sir, mine included. He bashfully smoothed his wild, tangled hair.

“I only had enough for myself at the time…”

The air turned cold again. Perfected Being Hyeoncheon continued.

“Regardless, the Great Sir helped us greatly. He gave me and all the Disciples of our sect a place to hide for a while and treated the wounded.”

It was said that a master could recognize a master.

At first, Perfected Being Hyeoncheon had been wary of the unidentified Supreme Peak master, but he hadn’t had any other real options. Before long, he’d come to feel the man’s sincere goodwill.

“While we were there, we also had an unexpected visitor.”

“An unexpected visitor?”

“At first, we thought the enemy had found our hideout and come to attack. But that wasn’t it. It turned out some men called the Seven Masters of White Bones had come to escort the Great Sir.”

“The Seven Masters of Baekma Bang,” Ma Junggeol interjected through gritted teeth.

“Oh, I must have mixed that up. The Black-Horse Seven?”

“I said the Seven Masters of Baekma Bang! Honestly, this is driving me insa—”

*Bap!*

I smacked Ma Junggeol on the back of the head without question or explanation and shut him up. Then I looked around.

Quite a few mounted figures were riding among the battlefield, their horses snorting roughly.

They wore relatively light leather armor and carried weapons like spears and crescent-bladed polearms. Now I could finally be sure who they were.

“Then could those people be…?”

“You’re thinking of the right people. They’re the horse caravans of Ningxia Province.”

Ma Junggeol, grimacing as he rubbed the back of his head, spoke in a tiny voice.

“More precisely, the horse caravans centered around Baekma Bang… Gah!”

He clamped his mouth shut when our eyes met. But this time, instead of hitting him, I patted him on the shoulder.

The Seven Masters of Baekma Bang had promised a few days ago that they would bring the Great Sir back. They’d returned with the horse caravans under their command, and thanks to them, we’d been able to deal a decisive, fatal blow to the enemies who were on the verge of collapse.

*So that’s how this worked out.*

I’d more or less forgotten they existed.

Or perhaps it would be more accurate to say I hadn’t expected much from them.

You always had to prepare for the worst in a battle, and the horse caravans, made up of former mounted bandits, weren’t exactly people you could trust.

But they had kept the promise they made to me, even if they were a little later than they’d planned. And with the Great Sir’s kindness, Perfected Being Hyeoncheon and the Kongtong Disciples had recovered from their injuries and returned to Gansu alongside thousands of horse-caravan riders.

Still, there was one question I couldn’t answer.

*So who the hell is that guy, really?*

I looked at the man they called the Great Sir, my eyes full of questions.

A moment ago, he’d clung to me and sobbed as if we were reuniting with a long-lost family. Now he was yawning widely just because the story had gotten a little long. As expected, he seemed far from sane.

Just as Ma Junggeol and his sworn brothers had told me.

And I quietly, secretly reached out toward the Great Sir.

A hand of detection, invisible and permitted only to me.

*Skill: Activate Qi Sense.*

*Whooooosh.*

The blue circle spread outward from me, at last reaching the Great Sir.
```
