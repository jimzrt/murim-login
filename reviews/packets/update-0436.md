<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0436.txt",
      "sha256": "654e377438904fb26818f974a2d5683f237a8389ea5de247a16a4ffaa516c0e6",
      "bytes": 14035
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "10a3d19185ae8c6de443ffca64cf4bf7038edb2c9915af98ae0d600525bd5134",
      "bytes": 1338
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "af8f09cfbf3dc86f8427aae7c1b7c58f798a979c253ce2219c30f39c5770f400",
      "bytes": 142655
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "c55cd201a141917ac58fdb89672c8cd597d2aa737441b38ba63dfcd2511d541c",
      "bytes": 944
    },
    {
      "path": "characters/Gung Gibang.md",
      "sha256": "0b82131bad7d98ea0b387b5aa6660ccf69e31e0b43bb7777bdbdefbf08b4f363",
      "bytes": 609
    },
    {
      "path": "characters/Hyuk Mujin.md",
      "sha256": "adda003271bd6c2619ced25ea9ec30669a39fce30ab562d814f8f80f0d0508b1",
      "bytes": 1108
    },
    {
      "path": "characters/Jeok Cheongang.md",
      "sha256": "456585494d0bcf1016e3701df563ceaaf7b6875ef4be9bd5e4f58bd3231ed046",
      "bytes": 1390
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "9e7b998af1e4d6ddaa964b9abd851cb28931f7dca8e1c2392702456f7a83ffa6",
      "bytes": 1239
    },
    {
      "path": "characters/Mae Jonghak.md",
      "sha256": "db74f2b818caaee5bbea23940eea827abf32772441bf8727af7e26ac31c8e046",
      "bytes": 1477
    },
    {
      "path": "characters/Mu Song.md",
      "sha256": "d5f22259b50c5ccb838d2c6e49257bd3c96ff922ecbd87f6b03244ba470ae919",
      "bytes": 792
    },
    {
      "path": "characters/Mungyeong.md",
      "sha256": "dc71dc529dabe15edda1abca54cb51731c6b1ffc771f26ec2b9cad56a4888a2a",
      "bytes": 666
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "e33e6a918562c60e3a36d8b6f1a05d941619317d40e8006c2d3c8f02fdcd682b",
      "bytes": 135962
    }
  ],
  "estimated_tokens": 12055
}
-->

# Durable State Update — Chapter 436

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity. Profile updates are maintenance, not chapter recaps: replace
existing fields to remove resolved events, stale travel/combat narration, and
duplicated facts. Preserve only stable identity, role, personality, voice,
relationships, and currently active unresolved/status facts. If a previous
detail no longer helps translate a future chapter, delete it. Never add a fact
merely because it appeared in the reading copy.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 436. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 12 concise items,
`open_questions` to at most 5 items, and
`temporary_decisions` to at most 5 items.
Keep the serialized context under 16384 UTF-8 bytes.
Use only chapter numbers through 436. Profile updates may replace only one
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
  "chapter": 436,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 436,
    "continuity_sources": [436],
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
    "Mungyeong's Slaughter Saint identity remains concealed beneath his medical-apprentice persona, though Jeok Cheongang recognizes it.",
    "Mungyeong continues traveling with Jin Taekyung's group without understanding his own reason for doing so.",
    "Jin Taekyung has opened his Middle Dantian.",
    "Jeok Cheongang considers Cheongpung superior to Jin Taekyung in pure martial talent.",
    "Jeok Cheongang thanked Mungyeong for saving Jin Taekyung.",
    "Jeok Cheongang destroyed one of Mu Song's special fast ships while responding to Jin Taekyung's alarm."
  ],
  "continuity_sources": [
    435,
    434
  ],
  "open_questions": [
    "Why does Mungyeong continue accompanying Jin Taekyung's group despite being unable to explain the impulse?",
    "How did Jin Taekyung open his Middle Dantian without Mungyeong or the others noticing?"
  ],
  "safe_through": 435,
  "temporary_decisions": [
    "Render 노야 as “Old Master” for Jin Taekyung's address to Jeok Cheongang.",
    "Keep Mungyeong's medical-apprentice voice cheerful and deferential, while his Slaughter Saint voice remains dry, terse, and threatening.",
    "Preserve the established renderings Middle Dantian, Heavenly Martial Physique, Turtle Breath Technique, Mingmen acupoint, and Flame Divine Palm."
  ],
  "version": 1
}
```

## Exact glossary matches

| 무림     | **Murim**          |
| 진위경    | **Jin Wikyung**    |
| 혁무진    | **Hyuk Mujin**     |
| 적천강    | **Jeok Cheongang** |
| 매종학    | **Mae Jonghak**    |
| 청풍     | **Cheongpung**     |
| 화왕     | **Fire King**                 | Jeok Cheongang |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 살성     | **Slaughter Saint**           | —              |
| 삼성     | **Three Saints**    |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 단전     | **dantian**                                      | Preserve the wuxia term                               |
| 신법     | **movement technique**                           |                                                       |
| 깨달음    | **enlightenment** / **insight**                  | Martial enlightenment                                 |
| 주화입마   | **qi deviation**                                 |                                                       |
| 살기     | **killing intent**                               |                                                       |
| 상태               | **Status**                     |
| 하남     | **Henan**              |
| 사천     | **Sichuan**            |
| 안휘     | **Anhui**              |
| 노부      | **this old man / I**                                            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 궁기방 | **Gung Gibang** | Beggars' Sect Successor Beggar and finalist. |
| 무송 | **Mu Song** | Lord of Water Dragon Stronghold and disciple of the Seafaring King. |
| 문경 | **Mungyeong** | Young medical apprentice and newly introduced passenger. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 가지 | **Go** | Song associated with Won Myunghoon. |
| 초절 | **supreme mastery** | Realm beyond Peak described as accessible only to the greatest martial artists. |
| 노야 | **Old Master** | Taekyung's private address for Jeok Cheongang. |
| 꼬리 | **the “tail”** | Codename for the Black Hunter traced by Butler Kim. |
| 호북 | **Hubei** | Province on Ju Gongsan's route from Guangdong to Henan. |
| 개방도 | **Beggars' Sect disciple** | Member of the Beggars' Sect. |
| 수룡채 | **Water Dragon Stronghold** | Major river stronghold belonging to the Yangtze River Channel League. |
| 장강 | **Yangtze** | The river controlled by the Yangtze River Channel League. |
| 광안 | **Guang'an** | Sichuan location where the party boards Mu Song's ship. |
| 오대 | **Five Squads** | Named Tang Clan organizational group in Tang Sadok's mobilization order. |
| 중단전 | **Middle Dantian** | Martial energy center opened by Jin during the battle. |

## Matched address pairs

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 진위경 | 적천강 | host_to_legendary_guest | Great Hero Jeok | formal-deferential | Introduces himself and pays respects to Jeok Cheongang as the Fire King. |
| 적천강 | 진위경 | elder_to_younger_family_head | you | gruff and teasing | Uses 자네 while mistaking Wikyung for Taekyung’s father and questioning his age. |
| 문경 | 무송 | survivor_to_savior_and_authority | Great Hero Mu Song | formal-deferential | Mungyeong credits Mu Song with saving him and asks him to spare Hwang Tae-gu. |
| 무송 | 문경 | stronghold_lord_to_young_passenger | you | gruff-but-considerate | Mu Song offers Mungyeong the right to decide Hwang Tae-gu's fate. |
| 청풍 | 문경 | martial_companion_to_medical_apprentice | Medical Apprentice | cheerful-polite | Cheongpung addresses Mungyeong as 의생님 while asking him to greet the Tang Clan. |
| 혁무진 | 궁기방 | squad_companion_to_Beggars_Sect_successor | Young Hero Gung | formal-polite, then pointed | Uses 궁 소협 while asking about the culprit and challenging Gung’s insults. |
| 문경 | 적천강 | old_acquaintances | Fire King | familiar and grave | The figure bearing Mungyeong’s name greets Jeok Cheongang by his established epithet. |
| 궁기방 | 혁무진 | squad_companions | you; that lunatic | insulting-casual | Gung Gibang mocks Hyuk Mujin's injuries and calls him a lunatic for attacking the Third Fiend. |
| 궁기방 | 청풍 | martial_companions | Young Hero Cheongpung | formal-polite | Gung Gibang uses 청 소협 while asking why Cheongpung is at the temporary clinic. |
| 진위경 | 막내 | older brother to younger brother | my youngest | intimate and informal | Jin Wikyung uses 막내야 affectionately for Jin Taekyung. |
| 무송 | 적천강 | junior_martial_artist_to_legendary_martial_master | Great Hero Jeok | formal-deferential | Mu Song respectfully refers to Jeok Cheongang as 적 대협 while worrying that Jeok dislikes him. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 435
- **Aliases:** Huashan Divine Dragon
- **Role:** Cheongpung is a twenty-three-year-old Huashan outsider, the grandson and Disciple of Sword Saint Mae Jonghak, and a Supreme Peak martial master known as the Huashan Divine Dragon.
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak is his grandfather and martial instructor, Baek Museong is his Martial Nephew, and Jin Taekyung and Hyuk Mujin are his Benefactors and companions while Taekyung is his only true martial rival; Tang Sadok has temporarily entrusted Mimi to him.

### Gung Gibang.md

# Gung Gibang (궁기방)

- **Safe through:** Chapter 377
- **Aliases:** Successor Beggar, Beggar Prince, pure-blooded beggar, ultimate beggar
- **Role:** Gung Gibang is the Beggars' Sect Successor Beggar and a unique eight-knot disciple.
- **Personality:** Vulgar, aggressive, and quick-tempered.
- **Voice:** Blunt, profane, and vividly threatening.
- **Relationships:** Rival finalist alongside Baek Woo and Zhuge Gyun; trades insults with Taekyung and is helping investigate Tang Taesang’s murder through Beggars’ Sect intelligence.

### Hyuk Mujin.md

# Hyuk Mujin (혁무진)

- **Safe through:** Chapter 377
- **Aliases:** Swift Wind Sword
- **Role:** Hyuk Mujin is a Level 50 First Rate martial artist who serves as Captain of the Jin Family's Gatekeepers and Vice Squad Leader of the Jin Dragon Squad.
- **Personality:** Young, disciplined, persistent, and talented. Values loyalty and respectable conduct, but is proud, glory-seeking, suspicious of Taekyung, and bluntly critical of the family's disgraced third son. He is an avid wuxia reader who sometimes mistakes fictional conventions for reality.
- **Voice:** Formal and clipped in official duties; blunt, moralizing, and occasionally incredulous with Taekyung.
- **Relationships:** Gatekeeper of the Jin Family and subordinate to Taekyung in the reconnaissance squad. Son of the Hyuk Family Textile Shop's owners; a younger sibling means he need not inherit the business. His loyalty to Taekyung and the reconnaissance squad strengthened through repeated battles and hardship.

### Jeok Cheongang.md

# Jeok Cheongang (적천강)

- **Safe through:** Chapter 435
- **Aliases:** Fire King; eighteenth Sect Leader of the Fire Gate Clan
- **Role:** Jeok Cheongang is a legendary wandering martial master and Jin Taekyung's Master.
- **Personality:** Secretive, cryptic, sharp-eyed, gruff, dryly teasing, and casually threatening or violent when dissatisfied. His meeting with Taekyung rekindled his will to live, making him determined to extend his life despite his illness.
- **Voice:** Sharp and ringing when calling out; otherwise gruff, dryly teasing, blunt, and threatening during interrogation or confrontation.
- **Relationships:** Jin Taekyung is his publicly acknowledged Disciple and intended heir to the Fire Gate Clan; Jeok recognizes Taekyung's Heavenly Martial Physique and has invested heavily in his growth. Jeok regards Mae Jonghak, the Sword Saint, as a kindred spirit and recognizes Cheongpung as Mae's grandson and successor. He was a close friend of Hong Dao, Shaolin's Abbot and Dharma King, whose death left him determined to act against the forces responsible. He rescued Jangcheon during an Anhui epidemic, accepted him as a Disciple, and regarded him as an only son and grandson despite Jangcheon becoming the murderer Jopil. Jeok is a long-standing rival of Peng Cheolhu, the Thunderbolt Saber King.

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 376
- **Aliases:** Junzi Sword
- **Role:** Jin Wikyung is the thirty-six-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan, the Alliance Leader who unified Shanxi Murim and Shanxi Province's foremost landowner and magnate.
- **Personality:** Calm, authoritative, and politically capable in public; protective and affectionate toward Taekyung beneath a stern mask. Takes responsibility for his people, acts decisively under pressure, and prioritizes family survival.
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate, proud, and occasionally exuberant with Taekyung.
- **Relationships:** Taekyung's eldest brother and future Family Head; Taekyung trusts him as a martial-arts mentor and family protector. Member and acting leader of the Jin Family of Taiyuan. Commands Wipeng and the family's forces. Has worked with Jeok Cheongang, who trained Taekyung under Wikyung's arrangement. Jin Mukyung is his younger brother and a potential successor alongside Taekyung.

### Mae Jonghak.md

# Mae Jonghak (매종학)

- **Safe through:** Chapter 374
- **Aliases:** Sword Saint
- **Role:** Sword Saint and Cheongpung's grandfather; more than forty years ago he sought Jeok Cheongang's help against the Demonic Cult, fought Jeok at Mount Jiuhua for seven days and seven nights, and drew with him; after the Great Faction War ended, he devoted himself to martial arts, reached Great Completion, attained higher enlightenment after encountering another wall, unexpectedly Returned to Youth, and traveled the world for a year under the name Jongni Chu while concealing his identity; at Mount Song he protected Cheongpung and attacked the Blood Lord with the divine Thirty-Six Plum Blossom Swords; after the Blood Lord escaped, he confirmed his identity to Jin Taekyung and Song Ho, and Song Ho identified Mae as the Great Hero who had saved his life.
- **Personality:** Not established in this chapter.
- **Voice:** Not established in this chapter.
- **Relationships:** Cheongpung's grandfather and martial instructor; taught him the Taeeul Miri Palm; secretly entered Huashan while its Sect Leader slept, left a dagger and handwritten note, and then went into hiding, prompting Huashan's search; fought Jeok Cheongang at Mount Jiuhua more than forty years ago and left after their draw; his old friend Hong Dao left him a letter identifying Jin Taekyung as the Morning Star who would drive away darkness.

### Mu Song.md

# Mu Song (무송)

- **Safe through:** Chapter 435
- **Aliases:** Ship-Fire Boy
- **Role:** Lord of Water Dragon Stronghold, a Peak master and the Seafaring King's second martial Disciple who controls major Yangtze river traffic in Sichuan and belongs to the Yangtze River Channel League's moderate faction.
- **Personality:** Ambitious, domineering, impatient with interruptions, and capable of pragmatic cooperation when circumstances demand it.
- **Voice:** Deep and low in private, shifting to dry authority or boisterous command when addressing subordinates and rivals.
- **Relationships:** He has carried Jin Taekyung's party and Mungyeong from Guang'an to Chengdu and agreed to send subordinates to help them return.

### Mungyeong.md

# Mungyeong (문경)

- **Safe through:** Chapter 435
- **Aliases:** None
- **Role:** Mungyeong is the legendary physician known as the Divine Physician and former Slaughter Saint, and he has sworn never to kill again.
- **Personality:** Compassionate, resolute, resourceful, and calm under extreme pressure.
- **Voice:** His Mungyeong persona is timid, deferential, and cheerful, while his Slaughter Saint voice is dry, impassive, and blunt.
- **Relationships:** Dong Feng is his Disciple, while Jeok Cheongang, Jin Taekyung, Cheongpung, and the two Sect Leaders know his Slaughter Saint identity.

## Korean source

```text
＃436화



장강(長江).

이름만 들어도 알 수 있듯이 장강의 규모, 특히 길이는 대륙에서도 둘째가라면 서러울 정도다.

사천, 중경, 호북, 안휘, 마지막으로 강소까지. 총 다섯 개 성을 가로지르는 해상 교통의 요충지이기 때문에 이번 여정에서도 큰 지분을 차지했다.

“우선 장강의 지류를 타고 호북(湖北)으로 간 뒤, 배에서 내려 육로로 하남까지 이동할 계획입니다.”

대강의 설명을 끝낸 진위경이 나를 포함한 일행들을 천천히 훑었다.

“혹시 질문 있으신 분 계십니까?”

쉭!

말이 끝나기가 무섭게 손 하나가 번쩍 올라갔다.

손 드는 속도만 보면 학문적 열의로 가득 찬 우등생이 따로 없지만, 정작 손의 주인은 무림에서도 전국구 깡패로 통하는 초절정 고수다.

“아까 전부터 노부가 궁금한 게 있는데.”

“세이 경청하겠습니다. 적 대협.”

“그러니까 지금 자네가 하는 말이…….”

적천강이 오만상을 쓰며 말을 이었다.

“이 염병할 장강에서 늙어 뒈지란 소리처럼 들리는데. 착각인가?”

역시 화왕이야. 아주 롸끈하지.

핸들이 고장 난 8톤 트럭처럼 들이받는 적천강식 화법에 진위경이 침을 꿀꺽 삼켰다.

“그럴 리가 있겠습니까, 적 대협. 단지 회의를 통해 나온 일정일 뿐입니다.”

“회의? 어떤 정신 나간 놈들이 이따위 일정을 짰어? 호북까지 가는 데에만 아무리 빨라도 칠 주야는 걸리겠다!”

“가장 위로는 검성 매종학 대협이 계시고, 그 아래로는 구파일방과 오대세가의…….”

“됐어. 더 이상 들을 필요도 없네.”

“예?”

“구파일방, 오대세가 놈들은 머릿속에 똥만 가득 찬 놈들이니 신경 쓸 것 없고, 매종학이한테는 노부가 잘 설명할 테니 지금이라도 일정 바꾸게. 온종일 물만 쳐다보고 있으려니까 주화입마가 걸릴 것 같아.”

한 줄 요약하자면, 배 째라는 소리다.

적천강이라서, 적천강만이 부릴 수 있는 강짜. 지금 이 자리에서 감히 그의 말에 토를 달 수 있는 사람은 없었다.

‘아, 한 사람 있긴 하구나.’

적천강도 순간 나와 비슷한 생각을 떠올렸음이 틀림없다.

슬쩍 고개를 돌린 그와 문경의 시선이 허공에서 부딪쳤다.

한심하다는 눈빛을 흘리는 문경을 바라보던 적천강이, 한마디를 툭 내뱉었다.

“마, 눈을 왜 그렇게 떠?”

“……!”

“대가리에 피도 안 마른 놈이. 확 그냥. 눈깔을 콕 찍어서 먹물을 쪽 빼 버릴라.”

이제 아주 대놓고 갈구는구나.

문경의 주먹이 파르르 떨렸다. 그의 실체를 아는 나로서는 등골이 서늘해지는 광경이었지만, 다른 사람들이 보기에는 달랐다.

장강 찍먹의 후유증으로 시름시름 앓고 있던 혁무진과 궁기방이 기어들어 가는 목소리로 말했다.

“왜 애를 가지고 그러십니까. 문경이 떠는 것 좀 보세요. 얼마나 심성이 여린 앤데……”

“저야 떠돌이 황구도 잡아먹고 그러지만, 문경이는 개미 한 마리도 못 죽이는 녀석입니다.”

“…….”

개미 죽일 시간에 사람을 죽였겠지.

지금까지 살성의 손에 목숨을 잃었다고 ‘공식적으로’ 알려진 사람들만 천 명이 넘는다고 들었다.

검에 마데카솔을 바르고 다녔어도 심성이 여리다는 소리를 들을 클라스가 아니다.

“네놈들…… 아니다. 됐다. 그냥 그렇게 살아라.”

어이가 없어 한 소리 하려던 적천강이 한숨을 푹 내쉬었다. 그러더니 돌연 나를 향해 방향을 틀었다.

“네 녀석은 왜 아무 말도 없느냐?”

“뭐가요?”

“뭐긴. 계속 이 지긋지긋한 물 위에 떠다니고 싶냐는 거지.”

“아, 그거요.”

잠깐 턱을 긁적이며 생각하던 내가 대답했다.

“전 나쁘지 않은데요.”

“뭣이!”

“막내야!”

적천강과 진위경의 희비가 엇갈렸다. 하지만 진위경을 도우려고 한 말이 아니라, 이게 내 진심이다.

“수뇌부들이 그렇게 결정한 데에는 그만한 이유가 있겠죠. 그리고 뭐, 보고 있으니까 풍경도 좋고.”

환경 오염이 없는 세상이다. 새벽녘만 되면 강을 뒤덮는 어스름하게 안개, 끝없이 펼쳐진 맑은 물을 보고 있노라면 가슴이 탁 트이는 것 같았다.

적천강이 의식불명 상태에 빠져 있을 때는 아무런 감흥도 느끼지 못했었는데…….

아무튼 지금은 잠시라도 조급함을 내려놓고 나 스스로를 돌아보며 가다듬을 필요가 있다.

‘그리고 조사해 봐야 할 일도 있고.’

두 세상에서 발견된 의문의 문양과 기호.

그에 따른 짐작이 사실인지 확인해 봐야 한다. 그러기 위해서는 무림과 현대를 오가며 처리해야 할 일들이 많았다. 육로로 이동하게 되면 그럴 시간이 현저하게 줄어들 것이다.

나는 적천강의 마음을 돌리기 위해 살살 구슬렸다.

“어차피 며칠 차이잖아요. 노야, 아니 스승님 몸도 생각하셔야죠. 무리하신 지 얼마 되지도 않으셨는데.”

“무리는 무슨. 누굴 다 죽어 가는 노인으로 보는 게냐?”

“……그럼 뭐. 이팔청춘입니까? 낭랑 십팔 세에요?”

“이놈이!”

적천강이 쌍심지를 켠 그 순간, 나는 황급히 입을 열었다.

“무공! 무공에 대한 가르침이 필요합니다!”

한 대 후려갈길 것처럼 올라왔던 손이 허공에서 우뚝 멈췄다. 그 틈을 놓치지 않고 내가 말을 이었다.

“근래에 얻은 깨달음이 있는데, 육로로 이동하게 되면 가르침을 받을 시간이 충분하지 않습니다.”

“가르침이라…….”

“저로서는 도저히, 머리를 쥐어 싸매고 고민을 해 봐도, 죽었다 깨어나도 알 수 없는 부분이 있어서 그렇습니다.”

“사실이냐?”

“예. 오직 천하에서 단 한 분. 스승님만이 알려 주실 수 있는 귀한 가르침이죠.”

적천강이 눈을 가늘게 떴다.

“육로로 경신법을 최대한 발휘한다면 며칠은 더 빨리 하남에 갈 수 있는데?”

“그게 가르침을 받는 것과 무슨 상관입니까?”

“상관이 있지. 일전에 네 녀석이 그러지 않았느냐. 검성 매종학이 노부보다 더 강할 것 같다고. 네 말대로라면 하루라도 빨리 하남에 도착해서 검성에게 물어보면 될 것 아니냐?”

놀리려고 슬쩍 던진 말인데 그걸 기억하네.

나는 시치미를 뚝 떼고 대답했다.

“잘못 들으신 것 같은데요. 저 혹시 그때 만취 상태였습니까?”

“아주 취랄을 하는구나.”

“저한테는 스승님이 늘 최곱니다.”

“그래?”

힐끗 문경을 곁눈질한 적천강이 물었다.

“그럼 살성에 비교하면 어떠하냐?”

“예?”

“살성 말이다. 삼성(三星)중에서도 사람 죽이는 것으로는 따라갈 수 없는 살성. 노부와 비교하면 어떻겠냐는 말이다.”

느껴진다. 내 대답을 흥미롭게 기다리는 사람들의 눈빛이.

그리고 누군가가 흘려보낸 은밀한 살기가.

‘에라, 시벌. 모르겠다.’

마른침을 꿀꺽 삼킨 나는 입을 열었다.

“좆밥이죠.”

“흠. 뭘 좀 아는 녀석인가?”

“제가 또 무잘알 아닙니까. 척 대보면 각 나와요.”

“커흠. 혓바닥에 기름칠이라도 했나, 평소에는 하지도 않던 아부를 늘어놓는구나. 노부가 그런 얕은수에 넘어갈 줄 아느냐?”

“……그런데 왜 웃고 계세요?”

무림 조커인가.

입꼬리가 귀까지 걸려 있던 적천강이 정색하며 얼굴을 굳혔다. 웃음을 참기 위해 움찔거리는 입가까지 감출 수는 없었지만.

“노부가 언제?”

“아닙니다. 어쨌건 그냥 이대로 쭉 가시죠.”

적천강도 내가 중단전을 개방한 사실을 알고 있는 상황. 잠시 고민하던 그가 입맛을 다셨다.

“옘병할. 아무리 그래도 물은 질색인데. 늘그막에 고생하게 생겼군.”

“…….”

아니 뭐, 전생에 불 포켓몬이었나. 이쯤 되면 별호를 화왕이 아니라 리자몽으로 고쳐야 하지 않나 싶다.

“뭐냐, 그 불손한 눈빛은?”

“제가요? 언제요?”

“됐다. 어차피 한두 번도 아니고. 너 같은 천둥벌거숭이에게 예의범절을 기대한 노부가 잘못이지.”

끌끌 혀를 찬 적천강이 진위경을 향해 고개를 돌렸다.

“다 들었지?”

“예. 불편함 없이 모시도록 하겠습니다.”

“그래서, 이 지긋지긋한 장강을 타고 호북에 가서 어쩔 셈인가? 괜히 이런 귀찮음을 감수할 만한 이유가 있겠지?”

“긴한 볼일이 있습니다.”

“볼일?”

“추후에 다시 말씀드려도 되겠습니까?”

적천강은 눈매를 좁혔지만 딱 거기까지였다. 진위경이 저렇게 말한다는 것은, 사람의 이목이 적을수록 좋은 기밀이라는 뜻이니까.

그리고 적천강은 눈치를 안 볼 뿐이지 아예 없는 사람은 아니었다.

“알겠네. 그럼 할 이야기는 끝났나?”

진위경이 공손히 포권을 취했다.

“고생하셨습니다.”

하지만 이 짧은 모임의 결과에 만족하지 못하는 한 사람이 있었다.

“자, 잠깐. 그럼 우리 수룡채의 쾌조선을 타고 호북까지 가시겠다는 말이오?”

배 주인, 무송의 말에 진위경이 대답하려던 그때. 적천강이 두 사람의 사이를 가로막았다.

“뭐 문제라도 있느냐?”

“저, 적 대협. 호북까지는 너무 멉니다. 바람을 잘 타도 칠 주야가 넘게 소요될 터인데…….”

“그렇게 오래 수채를 비워 둘 수는 없다?”

“예, 예. 바로 그겁니다!”

“몸통과 팔다리는 붙어 있는데 머리가 없어져서야 쓰나. 그럼 곤란하지.”

“그 말씀은……?”

“사천까지만 가.”

무송의 얼굴이 환하게 밝아졌다.

“감사합니다!”

“배는 놓고.”

“예?”

“노부가 조각배 타고 가리? 수부(水夫)는 가는 길에 구하면 해결될 테니, 쾌조선인지 뭔지는 놓고 돌아가게.”

잠시 침묵하던 무송이 힘겹게 입을 열었다.

“그…….”

“왜?”

“다시 생각해 보니 저와 제 수하들이 물심양면으로 모시는 것이 나을 것 같습니다.”

“허참, 굳이 그러지 않아도 되는데. 이미 배도 한 척 태워 먹어서 미안한데 이렇게 신세를 져도 되는지 모르겠군.”

“……불만 지르지 말아 주십시오.”

“그건 자네 하는 것 보고.”

이게 바로 대기업의 횡포인가.

살다 살다 수적이 안쓰러워 보이기는 처음이다.

슬픈 표정으로 포권을 취하고 물러나는 무송에게, 조용히 다가간 청풍이 손에 든 만두를 내밀었다.

그새 또 뭘 저렇게 많이 처먹었는지, 이미 양 볼은 터지기 직전이다.

“으에오.”

“……먹으라고? 지금 나 주는 건가?”

“에!”

실로 오랜만에 사람의 온기를 느낀 무송의 눈시울이 붉어졌다.

“고맙네. 청 소협.”

그리고 식은 만두를 한입에 쑤셔 넣은 그를 향해, 입 안에 든 것을 꿀꺽 삼킨 청풍이 활짝 웃어 보였다.

“맛있죠?”

“정말 그렇군. 근래 먹어 본 만두 중 가장 맛있었네. 다음에도 종종 얻어먹어야겠어.”

“그게 마지막이었어요.”

“마지막 남은 만두를 내게 주다니. 청 소협 그대는 도대체……!”

“할아버지가 그러셨어요. 좋은 것이 있으면 다른 사람과 나눠야 한다고요.”

지금까지 저 자식 혼자서 처먹은 걸 생각해 보면 개소리처럼 들리지만, 그 사실을 모르는 무송은 적잖이 감격했다.

“고맙네, 청 소협. 대화도 몇 번 나누지 못했는데 이리 신경 써 주다니. 나는 그것도 모르고…… 크흑.”

그리고 무송이 느낀 감격은 그리 오래가지 못했다.

“할아버지께서는요, 그런 말씀도 하셨어요. 마지막 만두를 먹은 사람이 다음 만두를 사 와야 한다고요!”

“……?”

“……?”

“하루만 더 가면 광안(廣安)이라는 곳이 나오는데요, 그곳 시장에서 파는 만두가 정말 맛있어요. 제가 일 년 동안 천하를 유람했을 때 그 만두 때문에 달포 동안이나 머물렀, 아. 그게 아니라 할아버지께서 그곳은 꼭 들러야 한다고 하셨어요! 만두를 마지막으로 먹은 사람이 잔뜩 사 와야 한 대요!”

“…….”

“…….”

무서운 새끼.

이제는 할아버지까지 팔아서 만두를 처먹으려고 하는구나.

그 광경을 지켜보던 궁기방은 훌륭한 개방도가 될 거라며 중얼거렸고, 광안 만두 맛집을 들르게 생긴 무송은 사람에 대한 신뢰를 모두 잃어버린 얼굴로 대답했다.

“알겠소.”

“와아! 할아버지께서 기뻐하실 거에요!”

저게 사람인가.

끝이 보이지 않는 인성에 경악하고 있던 그때였다.

“몸이 안 좋아 보이시는데. 잠깐 진료를 봐 드려도 될까요?”

좆밥. 아니 문경이 걱정스러운 얼굴로 나를 바라보고 있었다.

한 손에 숨겨 둔 대침을 내 허리에 바짝 댄 채.

“어. 아냐. 아냐. 난 아무렇지도 않…….”

“몸이 안 좋아 보이시는데. 잠깐 진료를 봐 드려도 될까요?”

“진짜 괜찮…….”

“몸이 안 좋아 보이시는데. 잠깐 진료를 봐 드려도 될까요?”

“…….”

쪽팔리지만, 방금 살짝 지린 것 같다.
```

## Final English reading copy

```markdown
# Chapter 436

The Yangtze.

As its name alone suggests, the Yangtze was enormous. In terms of length especially, few rivers on the continent could compare.

It crossed five provinces in all—Sichuan, Chongqing, Hubei, Anhui, and finally Jiangsu. As a vital hub of waterborne transportation, it would occupy a large portion of our journey.

“Our current plan is to follow one of the Yangtze’s tributaries to Hubei, then disembark and continue overland to Henan.”

After finishing his rough explanation, Jin Wikyung slowly looked over the group, including me.

“Does anyone have any questions?”

Whoosh!

The instant he finished speaking, one hand shot into the air.

Judging by the speed with which it went up, its owner looked like an honors student bursting with academic enthusiasm.

In reality, the hand belonged to a Supreme Peak master known throughout Murim as a nationwide thug.

“There’s something this old man has been wondering about for a while.”

“I’m all ears, Great Hero Jeok.”

“So what you’re saying is…”

Jeok Cheongang continued with a deeply sour expression.

“It sounds like you’re telling us to grow old and die on this damn Yangtze. Am I mistaken?”

That was the Fire King for you. He really knew how to bring the heat.

Jin Wikyung swallowed hard at Jeok Cheongang’s way of speaking, which came crashing forward like an eight-ton truck with a broken steering wheel.

“How could that be, Great Hero Jeok? This is simply the itinerary decided upon in our meeting.”

“A meeting? What kind of lunatics came up with this schedule? Even at the fastest pace, it’ll take seven days and nights just to reach Hubei!”

“At the top, we have Great Hero Sword Saint Mae Jonghak, and beneath him, the Nine Sects and One Gang and the Five Great Families…”

“That’s enough. I don’t need to hear any more.”

“Pardon?”

“The Nine Sects and One Gang and the Five Great Families are all idiots with nothing but shit in their heads, so forget about them. I’ll explain things properly to Mae Jonghak myself. Change the itinerary while there’s still time. Staring at water all day is going to give me qi deviation.”

In short, he was telling them to do their worst.

It was the kind of bullying only Jeok Cheongang could get away with. Not a single person here dared object to him.

*Ah. There was one person who could.*

Jeok Cheongang must have had the same thought, because he subtly turned his head.

His gaze met Mungyeong’s in midair.

Mungyeong looked back at him with an expression that clearly said *pathetic*.

Jeok Cheongang stared at him, then tossed out a single remark.

“Hey, what are you looking at me like that for?”

“…”

“You little punk, you’re still wet behind the ears. I ought to poke your eyes out and drain all the ink from them.”

He was openly laying into him now.

Mungyeong’s fist trembled.

As someone who knew his true identity, I found the sight chilling. To everyone else, however, it looked entirely different.

Hyuk Mujin and Gung Gibang, who had been languishing from the aftereffects of sampling the Yangtze, spoke in faint, faltering voices.

“Why are you picking on the boy? Just look at Mungyeong shaking. He’s such a gentle soul…”

“I may eat stray yellow dogs, but Mungyeong couldn’t kill an ant.”

“…”

He probably killed people during the time it took to kill an ant.

I had heard that more than a thousand people had been ‘officially’ declared dead at the hands of the Slaughter Saint.

Even if he went around with antibiotic ointment smeared on his sword, he wasn’t exactly the sort of person one would call gentle.

“You lot… No. Forget it. Just keep living like that.”

Jeok Cheongang had looked ready to say something, but he let out a deep sigh instead. Then, all of a sudden, he turned toward me.

“Why are you saying nothing?”

“About what?”

“What do you think? Do you really want to keep floating around on this miserable water?”

“Oh, that.”

I scratched my chin and thought for a moment before answering.

“I don’t mind it.”

“What!”

“Little Brother!”

Jeok Cheongang and Jin Wikyung’s expressions swung in opposite directions. But I hadn’t said it to help Jin Wikyung. I meant it.

“There must be a reason the people in charge decided on this route. Besides, the scenery is nice.”

This was a world without environmental pollution. Whenever dawn came and a hazy mist covered the river, looking out over the clear water stretching endlessly into the distance made me feel as though my chest were opening up.

When Jeok Cheongang had been unconscious, I hadn’t felt anything at all.

But now…

Regardless, I needed to set aside my impatience for a while and take the time to reflect and collect myself.

*And there are things I need to investigate.*

The mysterious patterns and symbols found in both worlds.

I had to find out whether my suspicions about them were correct. To do that, I had a lot to take care of while going back and forth between Murim and the modern world. If we traveled overland, the time available for that would be drastically reduced.

I tried to gently coax Jeok Cheongang around.

“It’s only a difference of a few days. Old Master—no, Master, you need to think about your health too. It hasn’t been long since you pushed yourself so hard.”

“What do you mean, pushed myself? Do you think this old man is on his deathbed?”

“Then what? Are you sixteen again? Eighteen and in the prime of youth?”

“You little bastard!”

The moment Jeok Cheongang’s eyes lit up, I hurriedly opened my mouth.

“Martial arts! I need instruction in martial arts!”

The hand that had risen as though to smack me stopped in midair.

I didn’t miss the opening and continued.

“I’ve gained some insight recently. If we travel overland, there won’t be enough time for you to teach me.”

“Instruction…”

“There are parts I could never understand on my own, no matter how hard I rack my brain over them—even if I died and came back to life.”

“Is that true?”

“Yes. It’s precious instruction that only one person in all the world can give me—my master.”

Jeok Cheongang narrowed his eyes.

“If we use movement techniques to our fullest overland, we could reach Henan several days earlier.”

“What does that have to do with receiving instruction?”

“It has everything to do with it. Didn’t you say before that you thought Sword Saint Mae Jonghak might be stronger than this old man? By your logic, shouldn’t you reach Henan as quickly as possible and ask the Sword Saint?”

I had tossed that out to tease him, but he remembered it.

I pretended not to know what he was talking about.

“You must have heard me wrong. Was I drunk out of my mind that day?”

“What a load of drunken bullshit.”

“To me, Master, you’re always the best.”

“Is that so?”

Jeok Cheongang glanced sideways at Mungyeong before asking,

“Then how do I compare to the Slaughter Saint?”

“What?”

“I mean the Slaughter Saint. The one among the Three Saints who has no equal when it comes to killing people. How do I compare to him?”

I could feel the people around me waiting with interest for my answer.

And I could also feel someone discreetly leaking killing intent.

*Ah, fuck it. I don’t know.*

I swallowed hard and opened my mouth.

“He’s a total fucking pushover.”

“Hm. Perhaps this boy knows what he’s talking about.”

“I’m something of a martial arts expert myself, you know. I can size someone up at a glance.”

“Ahem. Did you grease your tongue? You’re showering me with flattery you never use normally. Do you think this old man will fall for such a shallow trick?”

“…Then why are you smiling?”

Was he Murim’s Joker?

Jeok Cheongang’s smile stretched all the way to his ears, but he immediately straightened his face. He couldn’t quite hide the corners of his mouth twitching as he struggled not to laugh.

“When did I smile?”

“No, never mind. In any case, let’s just keep going like this.”

Jeok Cheongang already knew that I had opened my Middle Dantian. He considered it for a moment, then smacked his lips.

“Damn it. Even so, I hate water. Looks like this old man will be suffering in his twilight years.”

“…”

Had he been a Fire Pokémon in his previous life?

At this point, perhaps he should change his sobriquet from the Fire King to Charizard.

“What’s with that disrespectful look?”

“Me? When did I do that?”

“Forget it. It isn’t the first or second time, anyway. It was my mistake for expecting manners from an uncouth little brat like you.”

Jeok Cheongang clicked his tongue and turned toward Jin Wikyung.

“You heard everything, didn’t you?”

“Yes. We will see to it that you are kept comfortable.”

“So what are you planning to do after taking this miserable Yangtze to Hubei? There must be a reason worth enduring this much trouble.”

“We have an important matter to attend to.”

“An important matter?”

“Would it be all right if I told you later?”

Jeok Cheongang narrowed his eyes, but that was all.

If Jin Wikyung was speaking that way, it meant the matter was confidential—something better discussed with fewer ears around.

Jeok Cheongang might not care about other people’s reactions, but he wasn’t completely oblivious to them.

“Understood. Then are we finished here?”

Jin Wikyung politely clasped his hands.

“Thank you for your hard work.”

But one person was dissatisfied with the results of this brief meeting.

“W-wait a moment. Are you saying you intend to take our Water Dragon Stronghold’s fast ship all the way to Hubei?”

Just as Jin Wikyung was about to answer Mu Song, the owner of the ship, Jeok Cheongang stepped between them.

“Is there a problem?”

“Great Hero Jeok, Hubei is much too far. Even with a favorable wind, it will take more than seven days…”

“You can’t leave the stronghold empty for that long?”

“Yes, yes! Exactly!”

“A body can’t function with its limbs attached but its head missing. That would be a problem.”

“What does that mean…?”

“Go as far as Sichuan.”

Mu Song’s face brightened.

“Thank you!”

“Leave the ship behind.”

“What?”

“Am I supposed to travel in a skiff? We can find sailors along the way. Leave this fast ship—or whatever it’s called—and go back.”

Mu Song fell silent for a moment before managing to speak.

“Well…”

“What?”

“Now that I think about it, it would be better for me and my subordinates to escort you with every effort.”

“Good heavens, that really isn’t necessary. I already feel bad about burning one of your ships, so I’m not sure whether I should impose on you like this.”

“…Please don’t set anything else on fire.”

“That depends on how you behave.”

Was this the tyranny of a major corporation?

In all my life, this was the first time I had ever felt sorry for a river bandit.

As Mu Song withdrew with a sorrowful expression after clasping his hands, Cheongpung quietly approached him and held out the dumpling in his hand.

Who knew how much he had eaten in the meantime? Both his cheeks were already on the verge of bursting.

“’Ave it.”

“…Are you telling me to eat it? Are you giving it to me?”

“Yeah!”

Feeling the warmth of human kindness for the first time in ages, Mu Song’s eyes grew misty.

“Thank you, Young Hero Cheongpung.”

Then he stuffed the cold dumpling into his mouth in one bite.

After swallowing what he had been chewing, Cheongpung smiled brightly.

“Tasty, right?”

“It truly is. It’s the most delicious dumpling I’ve eaten in a long time. I’ll have to get some from you again sometime.”

“That was the last one.”

“What? You gave me the last dumpling? Young Hero Cheongpung, you…”

“My grandpa told me that when you have something good, you should share it with other people.”

Considering how much he had eaten by himself until now, it sounded like complete bullshit. But Mu Song didn’t know that, and he was deeply moved.

“Thank you, Young Hero Cheongpung. We’ve barely even spoken, yet you’ve gone out of your way to do this for me. I didn’t know that… Sniff.”

Mu Song’s gratitude did not last long.

“My grandpa also told me something else. Whoever eats the last dumpling has to buy the next dumplings!”

“…”

“…”

“If we travel for one more day, we’ll reach a place called Guang’an. The dumplings sold in the market there are really good. When I traveled around the world for a year, I stayed there for a whole month because of those dumplings. Ah, no, that’s not what I meant. Grandpa said we absolutely had to stop there! He said whoever ate the last dumpling had to buy a whole bunch more!”

“…”

“…”

What a terrifying little bastard.

Now he was even using his grandfather to get more dumplings.

Gung Gibang, who had been watching the scene, muttered that Cheongpung would make an excellent Beggars’ Sect disciple.

Mu Song, who looked as though he was about to visit the Guang’an dumpling shop, answered with every ounce of trust in humanity drained from his face.

“Understood.”

“Yay! Grandpa will be happy!”

Was that even human?

I was still horrified by the depths of his character when—

“You don’t look well. May I examine you for a moment?”

Fucking pushover—no, Mungyeong was looking at me with concern.

He had a large acupuncture needle hidden in one hand, pressed right against my waist.

“Uh, no. No, I’m fine. I’m not feeling—”

“You don’t look well. May I examine you for a moment?”

“I’m really fi—”

“You don’t look well. May I examine you for a moment?”

“…”

It was humiliating, but I think I may have wet myself a little.
```
