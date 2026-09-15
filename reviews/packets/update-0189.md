<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0189.txt",
      "sha256": "fa8b20012cf282f8807e8a1f1aaa68c01d495d4023f1553bfe806de6f8842636",
      "bytes": 14302
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "4f83adcb347a6cba476dc881720c6197b833fb73235923e2bd939b0cab920edd",
      "bytes": 3979
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "af2ab90cf53b36920cd2e27815873425960b2c43253f079f3ce9853ae0424907",
      "bytes": 47675
    },
    {
      "path": "characters/Baek Museong.md",
      "sha256": "e16eca0617fd10c098f2a8353e6582860c20469688a72d68b695ef97a00198d9",
      "bytes": 781
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "14cbe3b63dbfaa472da1f348b0e0e72a63aa7f7344b3f4496671696b3c2c60e9",
      "bytes": 2091
    },
    {
      "path": "characters/Chulwoo.md",
      "sha256": "ee15896bcef4bde535ee2d285bf00ecd3a9993ecfa0f6805157ef28a4f6674e1",
      "bytes": 1068
    },
    {
      "path": "characters/Eunhyang.md",
      "sha256": "017d325bf33258d2c00d4019ee2c8956538fbb56f2fb3585dcedb8d9b750d39c",
      "bytes": 743
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "1b2dc1b6a08fc66b12acb2558e9ebd3d99d8d5feba69efdc31ad9b5edacd3879",
      "bytes": 25015
    },
    {
      "path": "characters/Jin Wikyung.md",
      "sha256": "8c302c9e028003039257f40db62a5485d16a20672f9ed799c13e0d83dd2075bd",
      "bytes": 8320
    },
    {
      "path": "characters/Jintae.md",
      "sha256": "e95795fa7e5d552421eb9fadf1ad17fc2bdc860f6b97a463afdd277e924f39b9",
      "bytes": 622
    },
    {
      "path": "characters/Lee Seowol.md",
      "sha256": "28ba8604747bc7511e048c57b9002447c50306c9d27c20129f515cce0d2939bb",
      "bytes": 1458
    },
    {
      "path": "characters/Wolhwa.md",
      "sha256": "eb61ee6411e3a39cea030e13b95d5ef89d67764f76d24914f985dfc59150639f",
      "bytes": 2457
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "a0b1ceefa72870f94f4191b74506ac340b22b331f187c8e0f0baa7484c7afd16",
      "bytes": 40422
    }
  ],
  "estimated_tokens": 34513
}
-->

# Durable State Update — Chapter 189

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 189. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 189. `profile_updates` may replace one exact, uniquely occurring
complete line in a listed profile, and only an Aliases, Role, Personality, Voice, or
Relationships line. Use `profile_creations` only for a newly introduced named
character without a listed profile. Filenames must be plain `.md` basenames.
`names` contains only newly required Korean-to-English rows; Korean keys must occur
in the source. `address_pairs` contains only newly required speaker→addressee rows;
each Korean key must occur in the source or already appear in the address ledger,
and at least one endpoint must occur in the source (first-person narrators may be
ledger-only). Speaker and addressee must be Hangul source spellings (Arabic digits
allowed in titles such as 1팀장; do not romanize). Do not invent risk-register rows. Beat
plot paragraphs are plain strings; continuity and translation decisions are concise
list items.
Return this exact shape:

{
  "chapter": 189,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 189,
    "continuity_sources": [189],
    "active_continuity": ["active fact"],
    "open_questions": ["unresolved question"],
    "temporary_decisions": ["temporary translation decision"]
  },
  "names": [
    {"korean": "source spelling", "english": "English rendering", "notes": "brief note"}
  ],
  "address_pairs": [
    {
      "speaker": "speaker Korean",
      "addressee": "addressee Korean",
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

## Prior durable context

```json
{
  "active_continuity": [
    "Jeok Cheongang entrusted Jin Taekyung with the Flame Divine Palm manual and the Unnamed Sword forged from Ten-Thousand-Year Cold Iron.",
    "Jin Wikyung ordered Taekyung, Hyuk Mujin, and Cheongpung to keep the Fire King's entrusted items and all related information secret.",
    "Jin Wikyung described the entrusted objects as dangerous ghostly objects that awaken Greed and can drive people mad.",
    "Three Dark Heaven remnants survived interrogation under powerful restrictions; Wipeng was ordered to keep them alive as the Jin Family's only physical evidence.",
    "Jin Wikyung suspects Dark Heaven's attack on Shanxi Province was only the beginning and considers the Jin Family's victory suspiciously easy.",
    "Gong Yacheong, Socheon, and Soyul visited Taekyung at the Jin Family and were visibly healthier than before.",
    "Hyuk Mujin is on duty for the grand banquet and sent Socheon to deliver the banquet notice to Taekyung.",
    "Jin Wikyung admitted people beyond the invited guests to the grand banquet, and Taekyung was escorted to an honored seat with Baek Museong, Eunhyang, Chulwoo, and Cheongpung.",
    "Eunhyang's displayed Level is 75.",
    "More than three hundred Jin martial artists surrounded the Grand Training Ground and split a human curtain with a coordinated weapon display; the people behind it remain unidentified.",
    "Jin Wikyung publicly vowed that the Jin Family of Taiyuan would remain established in Shanxi three hundred years in the future as it had three hundred years in the past.",
    "Lee Seowol and the Mount Heng Sword Sect swore loyalty to the Jin Family of Taiyuan on New Year's Day, and the Jin Family accepted the sect as its vassal.",
    "Lee Seowol is eighteen and remains the current Sect Leader of the Mount Heng Sword Sect; Cheol Mubaek presented himself as its First Elder.",
    "Chulwoo is twenty-five, has fallen intensely in love with Lee Seowol, previously made a similar romantic declaration to another pretty third-generation disciple, and now publicly challenged Taekyung after seeing him interact with Seowol.",
    "Jin Wikyung is using the grand banquet to draw loyalty and gifts from former neutrals.",
    "Level 65 Choo Dohwan of the Iron Blood Sect, known as the Iron Fist, challenged Chulwoo and was defeated in roughly fifty exchanges.",
    "Chulwoo defeated at least fifteen duel challengers, including Level 25 Hwang Jinsu, before selecting Taekyung as his next opponent.",
    "The System created the Quest There Is a Man Who Loved You So Much for Chulwoo's challenge to Taekyung; refusing carries a massive penalty.",
    "Taekyung has unlocked access to Sound Transmission through reaching the Peak realm but has not yet learned to use it without practice."
  ],
  "continuity_sources": [
    188
  ],
  "open_questions": [
    "What is Dark Heaven ultimately seeking, and why was Shanxi Province targeted?",
    "Who are the three surviving Dark Heaven remnants, and what can be learned from them?",
    "Who or what is revealed when the human curtain at the Grand Training Ground splits apart?",
    "Does Jeok Cheongang intend to take Jin Taekyung as his Disciple?",
    "When will Jang Taebo complete Taekyung's commissioned weapon?",
    "Who has the Treasured Jade, or was it lost by Jopil?",
    "What consequences will follow Woo Hwangtae's conflict with Chulwoo and the Jin Family?",
    "Will Taekyung accept Chulwoo's duel and the associated Quest?"
  ],
  "safe_through": 188,
  "temporary_decisions": [
    "Render 화왕 as “Fire King.”",
    "Render 화염신장 as “Flame Divine Palm.”",
    "Render 만년한철 as “Ten-Thousand-Year Cold Iron.”",
    "Render 이름 없는 검 as “Unnamed Sword.”",
    "Render 암천 as “Dark Heaven.”",
    "Render 전음 as “Sound Transmission.”",
    "Render 대연무장 as “Grand Training Ground.”",
    "Render 주모 as “Lady of the House.”"
  ],
  "version": 1
}
```

## Existing names ledger

# Established Names

Binding Korean → English for names, titles, aliases, and forms established in
accepted chapters. Injected only when the exact Korean appears in the current
chapter. Overrides `compendium.md` on the same Korean key. Add a row at first
use. First use of an unlisted name or title almost always needs a footnote.

| Korean | Preferred English | Notes |
| ------ | ----------------- | ----- |
| 장삼 | **Jang Sam** | Bandit; personal name |
| 천력부 | **Heavenly Axe** | Epithet of Jang Sam; never romanize |
| 천관일 | **Sky-Piercing Strike** | Final form of the Jin Family's Spear Technique; 天貫軼 |
| 녹림십팔채 | **Eighteen Strongholds of Green Forest** | |
| 홍화루 | **Honghwaru** | Lower District Sect Shanxi branch; pleasure house in Taiyuan |
| 하연 | **Hayeon** | Jin Taekyung’s younger sister |
| 응현 | **Eung-hyeon** | Jin Family branch location |
| 산음 | **Saneum** | Jin Family branch location |
| 삭주 | **Sakju** | Jin Family branch location |
| 정양 | **Jeongyang** | Shanxi location |
| 혼주 | **Honju** | Shanxi location |
| 견정 | **Gyeonjeong** | Acupoint |
| 아문 | **Amun** | Acupoint |
| 봉안 | **Bongan** | Acupoint |
| 입동 | **Ip-dong** | Acupoint |
| 갱생권 | **Reformation Fist** | Jin Mukyung's named fist technique |
| 금나수 | **grappling technique** | Close-combat wrist-lock technique; rendered descriptively |
| 삼재검법 | **Three Calamities Sword Technique** | Sword technique Mukyung assumes Taekyung is pretending to use. |
| 약왕당 | **Medicine King Hall** | The Jin Family's medical hall. |
| 이공자 | **Second Young Master** | Title used for Jin Mukyung. |
| 수문각주 | **Master of the Gatekeeper Pavilion** | Office Hyuk Mujin is rumored to receive. |
| 공청석유 | **gongcheong seokyu** | Rare martial-arts elixir; the term also creates a petroleum pun. |
| 군자 | **junzi** | Confucian ideal of a morally upright gentleman. |
| 삼문협 | **Three Questions Gorge** | A distant gorge and route connecting Shanxi with Shaanxi and Henan. |
| 섬서 | **Shaanxi** | Province bordering Shanxi. |
| 삼공자 | **Third Young Master** | Title used for Jin Taekyung. |
| 맹주 | **Alliance Leader** | Leader of the regional Murim alliance. |
| 약왕당주 | **Medicine King Hall Master** | The unnamed physician who runs the Medicine King Hall. |
| 송검문 | **Song Sword Sect** | Small-to-medium sect in central Shanxi. |
| 송검문주 | **Sect Leader of Song Sword Sect** | Title held by Huang. |
| 귀검 | **Ghost Sword** | Wipeng's epithet. |
| 황 모 | **Huang** | Surname-style self-reference by the Sect Leader of Song Sword Sect. |
| 아스모데우스 | **Asmodeus** | Demon King referenced in Taekyung's sarcastic comparison; does not appear directly. |
| 낙류검 | **Falling Flow Sword** | Named sword technique discovered by Mukyung in the archives of Heaven's Gate Temple; its name evokes a waterfall. |
| 질풍십이권 | **Twelve Gale Fists** | Named fist technique Mukyung threatens to use against Taekyung. |
| 화염신장 | **Flame Divine Palm** | Jopil's deadly palm technique, noted when Taekyung compares Jopil with Mukyung. |
| 마혈 | **Paralysis Acupoint** | System condition label for temporary paralysis. |
| 아혈 | **Mute Acupoint** | System condition label preventing speech. |
| 분근착골 | **Tendon-Splitting and Bone-Twisting** | Cruel immobilization technique described by Mukyung. |
| 일문일살 | **One Question, One Kill** | Jopil's alias. |
| 군자검 | **Junzi Sword** | Epithet Jin Wikyung begins receiving after the war. |
| 칠득이 | **Childeuk** | Jin Family servant. |
| 천자문 | **Thousand Character Classic** | Classical text Childeuk cannot complete. |
| 천무지체 | **Heavenly Martial Physique** | Named physique or constitution mentioned hypothetically by Jin Mukyung. |
| 장칠득 | **Jang Childeuk** | Personal-name form of Childeuk; he is newly appointed as a martial artist directly under Jin Wikyung. |
| 최 팀장 | **Team Leader Choi** | Team Leader who owns the café where Taekyung signs a contract. |
| 명품충 | **Designer-Brand Junkie** | Display name used by Team Leader Choi in a text message. |
| 평화 | **Peace Guild** | Guild name. |
| 김 집사 | **Butler Kim** | Choi's butler and limousine driver. |
| 히말라야 | **Himalayas** | Mountain region referenced as the source of the bottled water. |
| 히말라야의 정수 | **Essence of the Himalayas** | System-named consumable that temporarily raises Intelligence. |
| 부천 | **Bucheon** | City with a dense concentration of Gates and Guild headquarters. |
| 강남 | **Gangnam** | Formerly valuable Seoul-area real estate. |
| 분당 | **Bundang** | Formerly valuable Korean real estate area. |
| 대한민국 | **Korea** | Country reference. |
| 순이 | **Sooni** | Former owner of Sooni's Super. |
| 순이네 수퍼 | **Sooni's Super** | The Peace Guild's Guild house. |
| 송 양 | **Miss Song** | The Peace Guild's final member; full identity not yet given. |
| 아레스 | **Ares Guild** | The leading Guild in Korea; formerly employed Team Leader Choi and Song Song. |
| 논산 | **Nonsan** | Location of Korea's Hunter training center. |
| 임혁준 | **Im Hyeokjun** | Im Kkeokjeong's personal name, shown in the System Level window. |
| 미노타우로스 | **Minotaur** | B-rank monster species. |
| 부천터미널 길드 | **Bucheon Terminal Guild** | Guild whose raid footage is shown. |
| 미노타우로스의 미로 | **The Minotaur's Labyrinth** | B-rank Gate. |
| 상동 길드 | **Sangdong Guild** | Mid-sized Guild near Bucheon that joins Peace Guild's first official raid. |
| 헌터 협회 | **Hunter Association** | Organization investigating the Bucheon Terminal Guild fatality. |
| 흑색 드레이크 | **Black Drake** | B-rank monster whose leather and spine are used for Taekyung's loaned equipment. |
| 장인의 흑색 드레이크 가죽 세트 | **Masterwork Black Drake Leather Set** | Peak-grade armor set loaned to Taekyung. |
| 장인의 검은 가시 창 | **Masterwork Black Thorn Spear** | Peak-grade spear loaned to Taekyung. |
| 출혈 | **Bleeding** | Effect with a 90% activation chance on a successful spear hit. |
| 니콜라스 | **Nicholas** | North American craftsman associated with the space-expansion suitcase. |
| K사 | **K Company** | Manufacturer of the space-expansion suitcase. |
| 혜린 | **Hye-rin** | C-rank female mage and member of Im Changsoo's Sangdong Guild team. |
| 청담동 | **Cheongdam-dong** | District mentioned as a luxury shopping location. |
| 투우사의 전신 갑옷 | **Matador’s Full-Body Armor** | Peak-grade armor equipped by Im Kkeokjeong; grants bonuses against bovine-type monsters. |
| 투우사의 방패 | **Matador’s Shield** | Peak-grade shield equipped by Im Kkeokjeong; can activate Taunt and Hallucination against bovine-type monsters. |
| 도발 | **Taunt** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 환각 | **Hallucination** | System effect that the Matador’s Shield can activate against bovine-type monsters. |
| 미노타우로스 전사 | **Minotaur Warrior** | Level-window designation for the first Minotaur encountered in the labyrinth. |
| 발설지옥 | **tongue-pulling hell** | Buddhist hell associated with punishment for liars and slanderers; explained in a footnote. |
| 껄떡쇠 | **Horndog** | Im Changsoo’s nickname for his womanizing. |
| 강원도 | **Gangwon Province** | Province named in Taekyung’s joke about the Minotaur’s next life. |
| 횡성 | **Hoengseong** | Place in Gangwon Province named in Taekyung’s joke. |
| 자일리톤 | **Xyliton** | Finnish equipment manufacturer whose custom helmet records video. |
| 유네스코 | **UNESCO** | Organization referenced in Taekyung’s cultural-heritage joke. |
| 일섬 | **One Annihilation** | Named spear technique Taekyung uses to kill the Boss Zone monster in one blow. |
| 미노타우로스 대전사 | **Minotaur Warrior** | Level 70 B-rank boss monster of The Minotaur's Labyrinth. |
| 임 팀장님 | **Team Leader Im** | Formal address for Im Changsoo used by a Sangdong Guild teammate. |
| 프로즌 | **Frozen** | Im Chunsoo's epithet as an A-rank ice mage. |
| K은행 | **K Bank** | Bank where Im Changsoo's transfer is reported. |
| 김정희 | **Kim Jeonghee** | Jin Taekyung and Hayeon's mother; restaurant kitchen worker |
| 아줌마 | **ajumma** | Familiar term for a middle-aged or married woman, used for Kim Jeonghee |
| 사장님 | **Boss** | Address for the restaurant owner; contextually rendered as ma'am in one reply |
| 김민수 | **Kim Minsu** | The restaurant owner's son; D-rank Hunter in Sangdong Guild. |
| 민수 | **Minsu** | Short form used for Kim Minsu. |
| 운기요상 | **Circulate Qi for Healing** | System-named skill that channels internal energy through another person's body to cleanse accumulated waste and restore health. |
| 하급 포션 | **Lesser Potion** | Low-grade healing potion issued as raid supplies; its System Grade is Third Rate. |
| 3차 각성자 | **third-awakening Hunter** | Hypothetical Hunter classification that would come after reawakening. |
| 재각성 | **reawakening** | Established Hunter awakening category described as having no further stage. |
| 피의 일주일 | **Bloody Week** | The hellish first week after Gates opened, during which casualties reached the tens of millions. |
| 전세 | **jeonse lease** | Korean lump-sum deposit lease used in the family's redevelopment-era housing history. |
| 박지훈 | **Park Jihoon** | Current name of Taekyung's former middle-school classmate; Hunter in Myeongdong Guild Team 1. |
| 박지황 | **Park Jihwang** | Jihoon's former name, revealed when Taekyung recognizes him. |
| 가람중 | **Garam Middle School** | Middle school attended by Taekyung and Jihoon. |
| 명동 길드 | **Myeongdong Guild** | Large Guild in which Jihoon belongs to Team 1. |
| 1팀장 | **Team 1 Leader** | Sangdong Guild's Team 1 leader and its only A-rank Hunter besides Im Chunsoo. |
| 희망 고시원 | **Hope Goshiwon** | The goshiwon listed as Taekyung's residence in the target report. |
| 기감 | **Qi Sense** | Taekyung's sensory technique; its range reaches seventy meters in this chapter. |
| 집파리 | **Housefly** | System label for a Level 1 fly familiar. |
| 검정파리 | **Black Blow Fly** | System label for a Level 1 fly familiar. |
| 금파리 | **Green Bottle Fly** | System label for a Level 1 fly familiar. |
| 패밀리어 | **Familiar** | System classification for the flies detected in Taekyung's home. |
| 김선희 | **Kim Seonhee** | Assistant Manager at the Ilsan Store |
| 대리 | **Assistant Manager** | Corporate title used by Kim Seonhee |
| 일산 | **Ilsan** | Location of the Store and Lafesta |
| 라페스타 | **Lafesta** | Shopping and entertainment district in Ilsan |
| 스토어 | **Store** | Restricted luxury retailer for magical goods and Hunter equipment |
| 쌀벌레 | **Rice Weevil** | Creature used by Hong Woojin as a Familiar |
| 링크 | **Link** | Mental connection between a mage and Familiar |
| 김희선 | **Kim Seonhee** | Source spelling variant for the established Assistant Manager Kim Seonhee at the Ilsan Store. |
| 여름이 | **Yeoreum** | Name Hayeon gives to the Level 2 kitten. |
| 김준수 | **Kim Junsu** | C-rank mental mage and Sangdong Guild Security Team’s sole Familiar mage. |
| 김권동 | **Kim Gwondong** | C-rank Sangdong Guild Security Team Hunter assigned to surveillance and disguise work. |
| 나비 | **Nabi** | Name used for the black kitten Familiar. |
| 고양시 | **Goyang** | City where the target previously visited a real-estate office. |
| 보안팀 | **Security Team** | Sangdong Guild’s surveillance and protection unit. |
| 보안팀장 | **Security Team Leader** | Unnamed leader coordinating the operation. |
| 최병일 | **Choi Byungil** | B-rank Security Team leader; his Level is in the mid-sixties. |
| 박형진 | **Park Hyungjin** | One of the C-rank Sangdong Guild watchers. |
| 오규현 | **Oh Gyuhyeon** | One of the C-rank Sangdong Guild watchers. |
| 이민철 | **Lee Mincheol** | One of the C-rank Sangdong Guild watchers. |
| 교관 | **Instructor** | Kim Hwajong's former Hunter Training Center role and address. |
| 헌터 훈련소 | **Hunter Training Center** | Training institution where Kim Hwajong served as an instructor. |
| 1번 훈련생 | **Trainee Number One** | Im Chunsoo's training call sign during his forced military identification. |
| 28연대 1대대 2중대 | **28th Regiment, First Battalion, Second Company** | Military unit designation shouted during Im Chunsoo's identification. |
| 사도세자 | **Crown Prince Sado** | Joseon crown prince used in the comparison for Jinho's haggard appearance; footnoted. |
| 박혁거세 | **Park Hyeokgeose** | Legendary founder of Silla, used in the comparison to Jinho emerging from the capsule; footnoted. |
| 열양공 | **heat-yang technique** | Mukyung's heat-based internal-energy technique. |
| 옥황상제 | **Jade Emperor** | Daoist deity invoked in Hyuk Mujin's prayer. |
| 원시천존 | **Primordial Heavenly Venerable** | Daoist deity invoked alongside the Jade Emperor. |
| 항산검문주 | **Sect Leader of the Mount Heng Sword Sect** | Title for Lee Seowol, the sect's current leader. |
| 산서제일미 | **Shanxi's foremost beauty** | Former reputation of Taekyung's mother. |
| 봉황객잔 | **Phoenix Inn** | Famous Shanxi inn with luxurious lodging, imperial-court cuisine, and a beautiful proprietress. |
| 계용옥미갱 | **chicken-and-corn soup** | Egg-thickened corn soup. |
| 계용옥미앵 | **chicken-and-corn soup** | Source spelling variant of 계용옥미갱 for the same dish. |
| 광수 | **Gwangsu** | First attacker at the Phoenix Inn; identified by the others after Taekyung punches him. |
| 적풍단 | **Red Wind Band** | Rising mounted-bandit power from the northern plateau. |
| 적풍단주 | **Red Wind Band Leader** | Unnamed leader of the Red Wind Band; commands two hundred followers. |
| 관제묘 | **Guandi Temple** | Shrine type mentioned in martial-arts novels. |
| 흑도 | **dark-path figures** | Generic category of underworld martial forces. |
| 오색귀 | **Five-Colored Ghosts** | Nickname for the five former subordinates of Jang Sam. |
| 이삼 | **Lee Sam** | Leader of the ten-man human-trafficking group; his Level window identifies him by this name. |
| 추종향 | **tracking scent** | Scent used to guide the messenger hawk. |
| 대동 | **Datong** | Shanxi location containing the Mount Heng Sword Sect branch destroyed by the Red Wind Band. |
| 토호단 | **Earth Tiger Band** | Mounted-bandit group formerly led by Pung Yang's subordinate. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 춘삼 | **Chunsam** | Lower District Sect martial artist serving as the carriage driver. |
| 철검대주 | **Iron Sword Squad Leader** | Title of the Mount Heng Sword Sect's Iron Sword Squad leader. |
| 대항산검문 | **great Mount Heng Sword Sect** | Expanded organizational form used for the Mount Heng Sword Sect. |
| 대동지부 | **Datong Branch** | Mount Heng Sword Sect branch in Datong. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 철 숙부 | **Uncle Cheol** | Lee Seowol's familial address for Cheol Mubaek. |
| 철 대협 | **Great Hero Cheol** | Respectful address for Cheol Mubaek. |
| 아가씨 | **Young Lady** | Former address used for Lee Seowol before she demands the title Sect Leader. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 산서괴협 | **Strange Hero of Shanxi** | Epithet referenced for the absent martial artist. |
| 녹림맹주 | **Green Forest Alliance Leader** | Leader title for the Green Forest Alliance. |
| 장강수로맹주 | **Alliance Leader of the Yangtze River Channel League** | Leader title for the Yangtze River Channel League. |
| 사마외도 | **demonic, heterodox arts** | Suspected martial-arts origin of Pung Yang's insidious forms. |
| 전서구 | **messenger pigeon** | Pigeon delivering the Lower District Sect's Jeongyang Branch report. |
| 절정 초입 | **early Peak** | Pung Yang's specific stage within the Peak realm. |
| 광칠이 | **Gwangchil** | Former mounted-bandit boss who took in Pung Yang and was later killed by a First Rate master. |
| 일류 초입 | **early First Rate** | Early stage of the First Rate realm. |
| 수라멸권 | **Shura Annihilating Fist** | Cheol Mubaek's single-successor martial art. |
| 항산권문 | **Mount Heng Fist Sect** | Alternate fist-sect designation used by Pung Yang for the Mount Heng defenders. |
| 화시 | **fire arrow** | Flaming arrow Lee Seowol fires to signal Cheol Mubaek. |
| 벽곡단 | **fasting pills** | Food-substitute pills found in the hidden cave where Cheol trained. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 적혈십이검 | **Crimson Blood Twelve Swords** | Peak-level martial arts manual discovered by Pung Yang. |
| 적혈심법 | **Crimson Blood Cultivation Technique** | Cultivation technique discovered by Pung Yang. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 태산압정 | **Mount Tai Presses Down on the Crown** | First move of the Three Calamities Sword Technique. |
| 나려타곤 | **Narye tagon** | Humiliating idiom comparing a fighter's evasive roll to a lazy donkey rolling on the ground. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 격산타우 | **Striking the Ox Across the Mountain** | Palm technique that transmits force through an intervening defense. |
| 북망산 | **Mount Beimang** | Mountain associated with burial grounds; used as a threat to send someone to their death. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 적혈십이도 | **Crimson Blood Twelve Sabers** | Pung Yang's domineering saber art; he has reached approximately seventy percent mastery. |
| 영단 흡수 | **Divine Pill Absorption** | System Quest created after Jin Taekyung takes the Blazing Flame Divine Pill. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 중상 | **Severe Injury** | System condition label causing a major drop in all stats. |
| 이름 없는 검 | **Unnamed Sword** | Oldest inventory item summoned when no item named 아무거나 can be found. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |
| 완전 회복 | **Full Recovery** | Immediate Quest success reward that heals Taekyung's injuries. |
| 뛰어난 금창약 | **Superior Wound Medicine** | Quest reward used to treat external injuries. |
| 십년하수오 | **Ten-Year He Shouwu** | Quest reward used to treat internal injuries. |
| 어제의 적, 오늘의 동지 | **Yesterday's Enemy, Today's Ally** | Quest completed when Taekyung delivers Wikyung's invitation. |
| 회광반조 | **final rally** | Terminal burst of apparent vitality before death. |
| 운칠기삼 | **seven parts luck and three parts skill** | Established Korean saying used in Taekyung's reflection. |
| 운구기일 | **nine parts luck and one part qi** | Taekyung's playful variation on 운칠기삼. |
| 혈랑검법 | **Blood Wolf Sword Technique** | Peak sword technique personally created by Lee Cheonbaek. |
| 혈랑보법 | **Blood Wolf Footwork** | Peak footwork technique personally created by Lee Cheonbaek. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 정양지부장 | **Jeongyang Branch Leader** | Leader of the Lower District Sect's Jeongyang Branch. |
| 혼주지부장 | **Honju Branch Leader** | Leader of the Lower District Sect's Honju Branch. |
| 총지부장 | **Chief Branch Leader** | Title Wolhwa holds within the Lower District Sect. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 진무보법 | **Jin Family's Manoeuvre Technique** | Named Jin Family footwork technique mastered by Taekyung. |
| 조장 | **Captain** | Hyuk Mujin's address for Taekyung as squad leader. |
| 숙부 | **Uncle** | Lee Seowol's shortened address for Cheol Mubaek. |
| 은원 | **gratitude and grudges** | Moral debts that must be repaid. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 아이템창 | **Item Window** | System window displaying an item's details. |
| 전서응 | **messenger eagle** | Emergency courier used by the Lower District Sect. |
| 폭혈단 | **Blood-Exploding Pill** | Demonic Cult pill said to kill the user after its time limit. |
| 구주 | **Nine Provinces** | Traditional geographic expression used in a threat. |
| 고원 | **Gaoyuan** | Plateau region in northern Shanxi. |
| 산서제일인 | **Shanxi's Number One** | Jin Wikyung's reputation for physical strength. |
| 금잔디 | **Geum Jandi** | Heroine of Boys Over Flowers, referenced in a sarcastic comparison. |
| 사술 | **dark arts** | Unorthodox means of obtaining power. |
| 마기 | **demonic qi** | Demonic energy discussed as a possible effect of the pill. |
| 선천지기 | **innate qi** | Vital energy said to be damaged by the pill's aftereffects. |
| 소음인 | **Soeumin** | One of the constitutional types in Sasang medicine. |
| 태양인 | **Taeyangin** | One of the constitutional types in Sasang medicine. |
| 주신 | **God of Drinking** | Wipeng's drinking epithet. |
| 야왕 | **Night King** | Rumored epithet for Jin Taekyung in Taiyuan's red-light district. |
| 화북 | **North China** | Regional designation used when discussing Shanxi drinking culture. |
| 산서제일가 | **foremost family in Shanxi** | Description of the Jin Family of Taiyuan's standing. |
| 장 노인 | **Old Man Jang** | Elderly villager who witnesses the Jin Family's arrival. |
| 현령 | **county magistrate** | County official who greets Jin Taekyung and delivers the City Lord's invitation. |
| 성주 | **City Lord** | Official who sends the invitation for a gathering with young prodigies. |
| 적토마 | **Red Hare** | Famous horse used in Hyuk Mujin's exaggerated comparison. |
| 여포 | **Lü Bu** | Historical warrior used in Hyuk Mujin's exaggerated comparison. |
| 성주의 초청 | **The City Lord's Invitation** | System Quest title. |
| 구파일방 | **Nine Sects and One Gang** | Major Murim grouping. |
| 오대세가 | **Five Great Families** | Major Murim grouping. |
| 주씨 | **Zhu** | Surname of the imperial ruling house. |
| 친왕 | **Prince** | Imperial title held by the Shanxi City Lord. |
| 천자 | **Son of Heaven** | Honorific title for the Emperor. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 태자 | **Crown Prince** | Title of the Emperor's older brother who was reportedly assassinated. |
| 석칠 | **Seokchil** | Middle-aged porter with nearly twenty years of experience. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 송 표두 | **Escort Chief Song** | Unnamed person responsible for the escort run. |
| 연화봉 | **Lotus Peak** | Peak on Huashan from which Cheongpung recently fled. |
| 빙당호로 | **candied hawthorn skewers** | Traditional fruit skewers coated in hardened sugar; explained in a footnote. |
| 하북 | **Hebei** | Province where Hyuk Family Textile Shop has a branch. |
| 혁가 포목점 | **Hyuk Family Textile Shop** | Taiyuan textile shop owned by Hyuk Mujin's parents; the largest in Taiyuan, with branches in Henan and Hebei. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |
| 메구미 | **Megumi** | Japanese name used in Taekyung's joke about the abbreviated dish name. |
| 산니백육 | **Garlic Pork** | Boiled pork sliced thin and served with garlic sauce. |
| 어향육사 | **Fish-Fragrant Shredded Pork** | Shredded pork dish. |
| 경장육사 | **Beijing Sauce Shredded Pork** | Shredded pork dish. |
| 규화계 | **Beggar's Chicken** | Named inn dish. |
| 매구 | **Maegu** | Waiter's shortened name for Maechae Guyuk. |
| 매채구육 | **Maechae Guyuk** | Pork belly with preserved mustard greens; the abbreviation is explained in a footnote. |
| 개방 | **Beggars' Sect** | Murim organization counted among the Nine Sects and One Gang. |
| 우진태 | **Woo Jintae** | Heir of the Seongun Escort Bureau and host of the Five Gates scions. |
| 우 소협 | **Young Hero Woo** | Honorific address for Woo Jintae. |
| 황 소저 | **Young Lady Hwang** | Honorific address for an unidentified young woman who is the only daughter of a martial sect. |
| 혁 아우 | **Little Brother Hyuk** | Familiar address for an otherwise unnamed male scion who calls Woo Jintae hyung. |
| 국주님 | **Chief** | Honorific title for the head of an Escort Bureau. |
| 촉금 | **Shu brocade** | Fine brocade brought from Sichuan. |
| 삼도문 | **Samdo Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |
| 궁귀문 | **Gunggui Sect** | One of the five former Five Gates sects annihilated at Eight Spring Gorge. |
| 성룡이 | **Seongryong** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 천우 | **Cheonwoo** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 명화 | **Myeonghwa** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 소혜 | **Sohye** | Name shown in a Level Window; one of the five current Five Gates scions. |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 도동파 | **Dodong Sect** | Fabricated sect claimed by Taekyung when Woo Jintae demands his affiliation. |
| 천진반 | **Tien Shinhan** | Fabricated personal identity claimed by Taekyung. |
| 왕가장 | **Wang Family Estate** | Family estate whose heir is one of the Five Gates scions; he uses sabers rather than sword arts. |
| 왕 공자 | **Young Master Wang** | Heir of the Wang Family Estate. |
| 신 소저 | **Young Lady Shin** | Young woman described as the only daughter of a martial sect. |
| 정 소협 | **Young Hero Jeong** | Address for one injured Five Gates heir; his given name is not stated. |
| 갈 소협 | **Young Hero Gal** | Address for one injured Five Gates heir; his given name is not stated. |
| 석 모 | **Seok** | Self-identification by Honghwa Inn's chief steward; his given name is not stated. |
| 석 총관 | **Chief Steward Seok** | Title and surname form used for Honghwa Inn's chief steward. |
| 칠매검 | **Seven Plum Sword** | Sword art practiced by the unnamed martial official at eight-tenths mastery. |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 정삼품 | **Third-Rank** | Official rank of the unnamed Assistant Military Commissioner. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 산서성부 | **Shanxi Provincial Office** | Government office where the City Lord resides west of Taiyuan. |
| 점소이 검신 되다 | **The Shop Assistant Becomes a Sword God** | Wuxia novel title read by Hyuk Mujin. |
| 아파야 무인이다 | **You Must Hurt to Become a Martial Artist** | Wuxia novel title read by Hyuk Mujin. |
| 무림의 아들 걸어서 구주팔황 세 바퀴 반 | **The Son of Murim Walks Three and a Half Rounds Around the Nine Provinces and Eight Wastes** | Wuxia novel title read by Hyuk Mujin. |
| 구주팔황 | **Nine Provinces and Eight Wastes** | Literary geographic phrase appearing in a wuxia novel title. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 이 첨사 | **Assistant Commissioner Li** | Address form for Li Feng |
| 홍 내관 | **Eunuch Hong** | Eunuch and Deputy Military Commissioner of Shanxi Province |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 도지휘사 | **Military Commissioner** | Provincial military commander's office |
| 종남삼수 | **Three Hands of Zhongnan** | Three renowned Zhongnan Sect martial artists invited to the gathering |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 풍운검군 | **Wind-and-Cloud Sword Lord** | Epithet of Gong Iljung, the Zhongnan Sect's Sect Leader. |
| 철혈문 | **Iron Blood Sect** | Henan sect mentioned by Gong Ilhyuk. |
| 오호검문 | **Five Tigers Sword Sect** | Henan sect mentioned by Gong Ilhyuk. |
| 태을미리장 | **Taeeul Miri Palm** | Palm technique taught to Cheongpung by Mae Jonghak. |
| 육합검 | **Six Harmonies Sword** | Huashan sword technique known by Cheongpung. |
| 매화검법 | **Plum Blossom Sword Technique** | Huashan sword technique Cheongpung performed at age ten. |
| 상청검 | **Supreme Clarity Sword** | Huashan sword technique listed among Cheongpung's knowledge. |
| 낙화추영장 | **Falling Flower Chasing Shadow Palm** | Huashan palm technique listed among Cheongpung's knowledge. |
| 산화무영수 | **Scattering Flowers Shadowless Hand** | Huashan hand technique listed among Cheongpung's knowledge. |
| 자하신공 | **Zaha Divine Technique** | Huashan internal-energy technique used by Cheongpung. |
| 태사부 | **Grandmaster** | Huashan title referring to Mae Jonghak. |
| 군림 | **The Reign** | Opening fragment of an incomplete wuxia novel title that Taekyung read through volume thirty-four. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 근위대 | **royal guard** | Guard unit protecting Prince Shangshan. |
| 근위대 갑옷 세트 | **Royal Guard Armor Set** | Armor set Li Feng offers Cheongpung. |
| 황태자 | **Crown Prince** | The Emperor's older brother in Taekyung's recollection. |
| 고평문 | **Gopyeong Sect** | Minor sect whose young sect leader is pressured by Taekyung. |
| 고평지부 | **Gopyeong Branch** | Proposed branch designation under the Jin Family of Taiyuan. |
| 상산왕의 증표 | **Prince Shangshan's Token** | Golden medallion awarded by Zhu Bao as the Quest Reward. |
| 선황 | **the late Emperor** | The former Emperor whom Hong Jin served. |
| 내관 | **palace attendant** | Hong Jin's former palace role; context identifies him as a eunuch. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 사서삼경 | **Four Books and Three Classics** | Confucian texts used to describe conventional scholarly learning. |
| 금성전장 | **Golden Star Exchange** | Financial institution that issued the thousand-nyang bank draft. |
| 전표 | **bank draft** | Negotiable draft used for the thousand-silver-nyang payment. |
| 은자 | **silver nyang** | Silver currency unit. |
| 철전 | **iron coins** | Lower-value coin currency used to compare the payment's value. |
| 은원보 | **silver yuanbao** | Small silver ingot given to Taekyung as pocket money. |
| 대국 | **Great Nation** | Political wording on the Jin Family's welcome banner. |
| 성군 | **sage king** | Desired form of rulership proclaimed for Prince Shangshan. |
| 대태원진가 | **great Jin Family of Taiyuan** | Formal exalted reference to the Jin Family of Taiyuan. |
| 평양 | **Pyongyang** | City invoked in Taekyung's communist-atmosphere joke. |
| 천하제일인 | **greatest under heaven** | Superlative martial distinction used in Hong Jin and Jin Wikyung's banter. |
| 고금제일인 | **greatest of all time** | Superlative martial distinction used in Hong Jin's exaggerated praise. |
| 비무행 | **dueling tour** | Cheongpung's planned journey to challenge the Ten Dragons and Phoenixes. |
| 청강검 | **blue-steel sword** | Cheongpung's sword. |
| 광염 | **light-flames** | Violet manifestation surrounding Cheongpung when he uses the Zaha Divine Technique. |
| 서안 | **Xi’an** | Historic city near Huashan. |
| 서악 | **Western Peak** | Name for Huashan among the Five Great Mountains. |
| 흑사파 | **Black Serpent Sect** | Dark-path gambling-den gang in Xi’an. |
| 화산일학 | **Huashan’s Lone Crane** | Epithet of Baek Museong. |
| 매화삼절 | **Three Plum Blossom Elites** | Collective title for the current Sect Leader’s three exceptional disciples. |
| 매화검수 | **Plum Blossom Swordsmen** | Huashan appointment held by its three elite disciples. |
| 검신 | **Sword God** | Alternate title used for Mae Jonghak; kept distinct from 검성, rendered Sword Saint. |
| 기해 | **qi sea** | Name for the dantian, the place where internal energy begins and gathers. |
| 임독양맥 | **Conception and Governor Vessels** | The paired vessels Taekyung attempts to open. |
| 근맥 | **Sinews and Meridians** | System attribute reduced by one after Taekyung's failed qi circulation. |
| 사해오호 | **Four Seas and Five Lakes** | Traditional geographic phrase used with the Nine Provinces and Eight Wastes. |
| 환골탈태 | **Bone Transformation** | Advanced transformation described as optional in martial-arts novels. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 청석 | **bluestone** | Extremely hard stone used for the training-ground floor. |
| 십팔반병기 | **eighteen traditional weapons** | Training weapons displayed on a rack. |
| 수련동 | **training hall** | Building located roughly two hundred jang from the training ground. |
| 찍고 땡 | **touch-and-go method** | Repeatedly reaching a destination and returning as an endurance exercise. |
| 홍가 | **Hong** | Unnamed middle-aged Jin Family martial artist who identifies himself by surname. |
| 진무량 | **Jin Muryang** | Founder of the Jin Family; legendary martial artist from roughly three hundred years earlier. |
| 천응 | **Heavenly Eagle** | Huge bird regarded as a spirit creature, said to have a wingspan exceeding one jang. |
| 혈교 | **Blood Cult** | Demonic organization named as a possible source of the intruder. |
| 강시 | **jiangshi** | Reanimated corpse from folklore; Childeuk and Hong mistakenly identify Taekyung as one. |
| 태초 마을 | **Taecho Village** | Place named by Taekyung immediately after surviving the fall. |
| 벽호공 | **Wall Lizard Technique** | Climbing martial art used to scale walls and cliffs. |
| 낙안봉 | **Falling Goose Peak** | Huashan peak exceeding five hundred jang; Cheongpung climbed it as a child. |
| 인피면구 | **human-skin mask** | Disguise made from peeled human facial skin. |
| 무재 | **martial talent** | Innate aptitude for learning martial arts. |
| 검성 수련 간접 체험기 | **Sword Saint Training: A Secondhand Experience** | Cheongpung's Peak-grade cliff-training Quest. |
| 검성 수련 간접 체험기-2 | **Sword Saint Training: A Secondhand Experience—2** | Linked Quest generated after the first training Quest succeeds. |
| 초보 수련자 | **Beginner Trainee** | System Title upgraded after the tenth cliff climb. |
| 중급 수련자 | **Intermediate Trainee** | System Title received after Beginner Trainee is upgraded. |
| 황하방 | **Yellow River Gang** | Organization involved in a dispute with the Sogong Sect. |
| 소공문 | **Sogong Sect** | Sect involved in a dispute with the Yellow River Gang. |
| 남부상회 | **Southern Merchant Guild** | Merchant organization whose matter is reported to Jin Wikyung. |
| 내당주 | **Inner Hall Master** | Title for the head of the Jin Family's Inner Hall. |
| 내외당 | **Inner and Outer Halls** | The Jin Family's two internal administrative divisions. |
| 세가 | **great family** | Murim category Jin Wikyung hopes the Jin Family will attain. |
| 복호권 | **Crouching Tiger Fist** | Huashan martial art Cheongpung uses during the spar. |
| 암향표 | **Dark Fragrance Drift** | Movement technique Cheongpung uses to evade Taekyung's attacks. |
| 천근추 | **Thousand-Catty Drop** | Technique Cheongpung identifies when Taekyung lifts the spear shaft beneath his foot. |
| 일권복호 | **One Fist Subdues the Tiger** | Named form of the Crouching Tiger Fist. |
| 매화권 | **Plum Blossom Fist** | Huashan fist technique Cheongpung uses in sparring. |
| 천응조 | **Heavenly Eagle Claw** | Huashan claw technique used by Cheongpung. |
| 봉미혈 | **Fengwei acupoint** | Acupoint around the ribs targeted by Cheongpung. |
| 태권도 | **Taekwondo** | Martial art Taekyung practiced as a child. |
| 태극 1장부터 8장까지 | **Taegeuk Forms 1 through 8** | Standard taekwondo pattern sequence Taekyung copied as a child. |
| 공수납백인 | **Empty-Hand Seizes the Blade** | Technique for catching an opponent's weapon between bare fingers. |
| 오행매화보 | **Five-Element Plum Blossom Steps** | Footwork technique Cheongpung combines with Dark Fragrance Drift. |
| 백전백패 | **Hundred Battles, Hundred Losses** | Taekyung's proposed teasing nickname for Mujin. |
| 너구리 | **Neoguri** | Instant-noodle brand used in Taekyung's flavor joke. |
| 진라면 | **Jin Ramen** | Instant-noodle brand used in Taekyung's flavor joke. |
| 푸라면 | **Puramyeon** | Instant-noodle brand used in Taekyung's flavor joke. |
| 매화오품지 | **Plum Blossom Five-Point Finger** | Five-finger technique Cheongpung uses during the duel. |
| 벽을 넘어서 | **Beyond the Wall** | System Quest generated during Taekyung's breakthrough. |
| 절정 고수 | **Peak Master** | System class awarded after Taekyung completes Beyond the Wall. |
| 테무르 | **Temur** | Northern Gaoyuan chieftain commanding one hundred tribespeople; claims descent from the khans. |
| 칭겐 | **Chinggen** | Northern Gaoyuan chieftain commanding one hundred tribespeople; restrains Temur. |
| 인도 | **Human Butcher** | Epithet of a mysterious Han Chinese mounted-bandit power commanding fifty subordinates. |
| 텡게르 | **Tengger** | Sky deity invoked by Temur. |
| 대칸 | **Great Khan** | Title of the former ruler whose descendants Temur and Chinggen claim to be. |
| 대초원 | **Great Steppe** | The steppe region from which Temur and Chinggen come. |
| 마유주 | **mare's-milk wine** | Fermented alcoholic drink offered at the gathering. |
| 게르 | **ger** | Traditional nomadic dwelling contrasted with Central Plains wooden buildings. |
| 한족 | **Han Chinese** | Ethnic designation used by the steppe chieftains. |
| 흑사 | **Black Sand** | Eyepatched middle-aged leader of the Black Sand Band; a newly introduced identity. |
| 흑사대 | **Black Sand Band** | Han-Chinese mounted-bandit force of one hundred. |
| 천풍단 | **Heavenly Wind Band** | Five-hundred-member northern plateau mounted-bandit force subordinate to Black Sand. |
| 천풍단주 | **Heavenly Wind Band Leader** | Leader operating under Black Sand's orders near Datong. |
| 하곡 | **Hequ** | Route and Jin Family branch targeted as the alliance's entry point into Shanxi. |
| 참마검 | **horse-chopping sword** | Heavy saber used by the Human Butcher; rendered descriptively. |
| 삼매진화 | **Samadhi True Fire** | Internal-energy flame demonstrated by the unnamed old man. |
| 귀환자 | **Returnee** | System Title |
| 명가의 자제 | **Scion of a Prestigious Family** | System Title |
| 승부사 | **Gambler** | System Title |
| 명장 | **Master Artisan** | Master craftsman capable of handling Ten-Thousand-Year Cold Iron |
| 가공되지 않은 만년한철 | **Unprocessed Ten-Thousand-Year Cold Iron** | System Item |
| 장인을 찾아라 | **Find the Master Artisan** | System Quest |
| 장태보 | **Jang Taebo** | Former Guild Leader of the Ironcraft Guild; now lives near Jeongyang and is sought as a Master Artisan. |
| 철기방 | **Ironcraft Guild** | Hubei guild composed mainly of skilled craftsmen and closely associated with the Nine Sects and One Gang. |
| 철기방주 | **Guild Leader of the Ironcraft Guild** | Title of the Ironcraft Guild’s leader; the current leader is Jang Taebo’s disciple. |
| 오향장육 | **five-spice pork** | Dish Cheongpung packed for the journey. |
| 항아 | **Hanga** | Local village boy who lives near Jang Taebo. |
| 구방표국 | **Nine-Room Escort Bureau** | Escort Bureau that supplies Jang Taebo with a fifty-year-old He Shou Wu every four months. |
| 하수오 | **He Shou Wu** | Traditional medicinal herb; a thirty-year-old specimen is offered to Jang Taebo. |
| 오십 년 묵은 하수오 | **Fifty-Year-Old He Shou Wu** | First Rate Spirit Herb shown in the System Item Window; can provide up to about two years of internal energy. |
| 불로초 | **Herb of Eternal Youth** | Spirit herb said to grant eternal youth and immortality. |
| 불로초를 찾아서 | **In Search of the Herb of Eternal Youth** | System Quest generated after Jang Taebo names the Herb of Eternal Youth. |
| 천검진인 | **Heavenly Sword True Person** | Taoist-style title of the current Sect Leader of Huashan, who once commissioned a sword from Jang Taebo. |
| 여의주 | **dragon pearl** | Legendary treasure requested by Jang Taebo. |
| 공청석유, 용의 발톱, 여의주 구하기 | **Get Gongcheong Seokyu, a Dragon’s Claw, and a Dragon Pearl** | Quest generated after Jang Taebo makes additional demands; Taekyung rejects it. |
| 천풍 | **Heavenly Wind** | Short form displayed on the Heavenly Wind Band's flag. |
| 장팔 | **Jang-pal** | Woodcutter who meets and helps the unnamed old man. |
| 장 씨 | **Jang** | Surname form used for the woodcutter Jang-pal. |
| 장가촌 | **Jang Family Village** | Clan village where Jang-pal lives. |
| 홍가촌 | **Hong Family Village** | Clan village said to be three hundred li from Jang Family Village. |
| 신령님 | **Mountain Spirit** | Jang-pal's mistaken address for the unnamed old man. |
| 장씨 | **Jang** | Unspaced source variant of 장 씨; surname form for Jang-pal. |
| 반박귀진 | **Returning to Simplicity** | Supreme Peak technique or phenomenon used by Jeok Cheongang. |
| 이형환위 | **Shifting Form and Position** | Supreme Peak movement or evasion technique used by Jeok Cheongang. |
| 허공섭물 | **Seizing an Object Through Empty Space** | Technique Jeok Cheongang uses to lift Jang Taebo remotely. |
| 백련정강 | **Baekryeon Jeonggang** | Extremely hard steel used to forge Hyuk Mujin's sword. |
| 강자지존 | **Might Makes Right** | Murim principle invoked as the basis for Mae Jonghak's challenge. |
| 꼰대 | **boomer** | Modern slang for a hidebound older person; used by Cheongpung. |
| 꼰머 | **boomer-brain** | Related slang term Cheongpung says has a similar meaning. |
| 국밥 | **gukbap** | Korean dish of rice served in hot soup; footnoted in the reading copy. |
| 부마도위 | **Imperial Son-in-Law** | Imperial title mentioned by Jang Taebo. |
| 천하오대세가 | **Five Great Families** | Expanded source form of 오대세가. |
| 열화신공 | **Fire Gate Divine Technique** | Secret internal cultivation technique of the Fire Gate Clan, preserved through one-person succession without leakage. |
| 장천 | **Jangcheon** | Name Jeok Cheongang gave to the orphan who later became Jopil; means “Vast Sky.” |
| 벌모세수 | **cleansing the sinews and washing the marrow** | Jeok Cheongang’s constitution-improving technique. |
| 상단전 | **upper dantian** | Advanced dantian whose opening signifies entry into the Martial Extremity realm. |
| 무극 | **Martial Extremity realm** | Realm associated with opening the upper dantian. |
| 창천검왕 | **Azure Sky Sword King** | One of the Ten Kings and the Grand Family Head of the Nangong Family. |
| 태상가주 | **Grand Family Head** | Title held by the Azure Sky Sword King as head of the Nangong Family. |
| 왕팔 | **Wangpal** | One of the youths who tried to take Jangcheon's dumpling. |
| 홍소칠 | **Hong Sochil** | One of the youths who tried to take Jangcheon's dumpling. |
| 소우평 | **So U-pyeong** | One of the youths who tried to take Jangcheon's dumpling. |
| 보옥 | **Treasured Jade** | Missing Fire Gate Clan treasure sought by Jeok Cheongang. |
| 우황태 | **Woo Hwangtae** | Chief of the Seongun Escort Bureau and Woo Jintae's father. |
| 수문각 | **Gate Guard Pavilion** | Jin Family gate complex at the main entrance. |
| 수문위사 | **gate guard** | Jin Family guard stationed at the gate. |
| 장주 | **Lord** | Title used for one of the Five Gates heads, as in 태 장주. |
| 패화권 | **Defeated Flower Fist** | Chulwoo’s epithet. |
| 산서기협 | **Shanxi Extraordinary Hero** | Epithet mentioned among the Jin Family’s known figures; distinct source spelling from 산서괴협. |
| 소림사 | **Shaolin Temple** | Temple invoked in Chulwoo’s comparison of Baek Museong’s conduct. |
| 화검봉 | **Flower Sword Phoenix** | Eunhyang’s epithet and one of the Three Plum Blossom Elites. |
| 화산말학 | **Huashan’s Last Crane** | Taekyung’s mistaken hearing of 화산일학; not a genuine epithet. |
| 매화손절 | **Plum Blossom Cutoff** | Taekyung’s mistaken hearing of 매화삼절; not a genuine title. |
| 하곡문 | **Hequ Sect** | Small sect led by Jang Se-pal. |
| 장세팔 | **Jang Se-pal** | Leader of the small Hequ Sect. |
| 양천 | **Yangcheon** | Shanxi-area location near which a small martial arts academy operates. |
| 노호검객 | **Roaring Fury Swordsman** | Fiery-tempered elder and top-five master of the Zhongnan Sect. |
| 청성파 | **Qingcheng Sect** | Sect named in Baek Museong's comparison about disciplinary rules. |
| 집법원 | **Disciplinary Hall** | Huashan body that handles violations of sect rules. |
| 대연무장 | **Grand Training Ground** | The Jin Family's largest training ground and the site of the grand banquet. |
| 주모 | **Lady of the House** | Title used in Wipeng's remark that Jin Wikyung lacks a wife or household mistress. |
| 일장로 | **First Elder** | Title Cheol Mubaek claims within the Mount Heng Sword Sect. |
| 이대 문주 | **second Sect Leader** | Lee Seowol's succession title as the Mount Heng Sword Sect's second Sect Leader. |
| 디그다 | **Diglett** | Pokémon species used in Taekyung's analogy. |
| 닥트리오 | **Dugtrio** | Pokémon species used in Taekyung's analogy. |
| 언더아머 | **Under Armour** | Modern sportswear brand mentioned in Taekyung's joke. |
| 추도환 | **Choo Dohwan** | Level 65 Iron Blood Sect martial artist known as the Iron Fist. |
| 철권 | **Iron Fist** | Choo Dohwan's epithet. |
| 상도문 | **Sangdo Sect** | Sect pledging itself to the Jin Family at the banquet. |
| 황진수 | **Hwang Jinsu** | Level 25 challenger from Hwang Family Manor. |
| 황가장 | **Hwang Family Manor** | Family estate represented by Hwang Jinsu. |
| 갈 모 | **Gal Mo** | Nameless wandering martial artist who challenges Chulwoo. |

## Existing address-pair ledger

# Established Address Pairs

Exceptional speaker → addressee forms established in accepted chapters.
Injected only when both endpoints are present in the current chapter: the
Korean appears in the source, or belongs to a matched compact profile.
Overrides generic relationship prose in character profiles for this pair.

| Speaker | Addressee | Kinship | Normal address | Speech level | Notes |
| ------- | --------- | ------- | -------------- | ------------ | ----- |
| 진태경 | 진무경 | younger_to_older_brother | hyung | casual-but-junior | Retain hyung for 형 in Taekyung's greeting; Mukyung then punishes the casual speech. |
| 진무경 | 진태경 | older_to_younger_brother | youngest | blunt-senior | 막내 / youngest; may taunt that lasting a quarter-hour would make Taekyung the older brother. |
| 진태경 | 진위경 | younger_to_eldest_brother | brother | familiar-but-respectful | Self-corrects from the personal name to kinship: “Jin Wikyung—I mean, my brother?”; 큰형 is eldest brother. |
| 진위경 | 진태경 | eldest_to_youngest_brother | youngest | affectionate-protective | Uses youngest-brother address; openly affectionate beneath a public mask. |
| 진태경 | 성진호 | junior_to_older_friend | Jinho hyung | casual-but-junior | Retain hyung for 형; Jinho is three years older. |
| 성진호 | 진태경 | older_friend | informal / younger-brother | teasing-senior | Speaks informally while demanding respect as the older friend. |
| 진태경 | 임꺽정 | junior_friend | Kkeokjeong hyung | casual-but-junior | After Im asks to be called hyung. |
| 임꺽정 | 진태경 | older_friend | hyung | hearty-casual | “Call me hyung. We’re not even that far apart in age.” |
| 위팽 | 진위경 | retainer_to_lord | my lord | deferential | 주공; Wipeng is Jin Wikyung’s personal guard. |
| 소천 | 진태경 | rescued_survivor_to_benefactor | Benefactor | deferential | Socheon repeatedly addresses Taekyung as 은인. |
| 진무경 | 진위경 | younger_to_older_brother | older brother | formal-but-blunt | Mukyung refers to Wikyung as 형 while remaining emotionally restrained. |
| 진위경 | 진무경 | older_to_younger_brother | little brother | affectionate-casual | Wikyung uses 아우야 and 무경아 with openly affectionate familiarity. |
| 진태경 | 공야청 | junior_to_respected_hero | Great Hero Gong | deferential | Taekyung consistently attaches 대협 when addressing Gong Yacheong. |
| 위팽 | 송검문주 | visitor_to_sect_leader | Sect Leader | formal-polite | Wipeng addresses the Song Sword Sect Leader respectfully while delivering the summons. |
| 송검문주 | 위팽 | sect_leader_to_visiting_master | Great Hero Wipeng | deferential | The Sect Leader addresses Wipeng as 위 대협 while fearing the Ghost Sword's power. |
| 진태경 | 월화 | junior_to_older_female_acquaintance | Wolhwa noona | casual-but-junior | Taekyung uses this address while speaking in his sleep or delirium. |
| 칠득이 | 진위경 | servant_to_lesser_family_head | Lesser Family Head | deferential | Childeuk repeatedly addresses Wikyung as 소가주님. |
| 진위경 | 칠득이 | lesser_family_head_to_servant | you | formal-but-familiar | Wikyung addresses Childeuk with 자네. |
| 진위경 | 장칠득 | lesser_family_head_to_direct_martial_artist | Martial Artist Jang | affectionate and ceremonious | Wikyung embraces and exuberantly praises Childeuk after acknowledging their minor misunderstanding. |
| 혁무진 | 진태경 | squad_subordinate_to_squad_leader | Squad Leader | deferential | Hyuk Mujin says he obeys only his squad leader's orders and identifies Taekyung as the Third Young Master. |
| 진태경 | 혁무진 | squad_leader_to_squad_subordinate | Mujin | familiar-and-commanding | Taekyung calls him 무진아 while summoning him from the driver's box. |
| 진태경 | 최 팀장 | guild_member_to_team_leader | Team Leader | deferential | Taekyung addresses Choi as 팀장님. |
| 최 팀장 | 진태경 | team_leader_to_guild_member | Taekyung | formal-but-familiar | Choi addresses him as 태경 씨. |
| 진태경 | 김 집사 | client_to_butler | Butler Kim | formal-deferential | Taekyung addresses him as 김 집사님. |
| 최 팀장 | 김 집사 | employer_to_butler | Butler Kim | formal-polite | Choi addresses him as 김 집사님. |
| 김 집사 | 진태경 | butler_to_hunter_client | Hunter | deferential | Butler Kim refers to Taekyung as 헌터님. |
| 임꺽정 | 송 양 | older_guild_member_to_younger_female_guild_member | Miss Song | hearty-casual | Im Kkeokjeong calls her 송 양. |
| 진태경 | 송송이 | guild_member_to_guild_member | Miss Song | formal-polite | Taekyung repeatedly uses 송이 씨 while introducing himself and attempting to court Song Song. |
| 송송이 | 진태경 | guild_member_to_guild_member | Taurus | casual-teasing | Song Song refers to Taekyung by his zodiac sign when calling him to the meal. |
| 진태경 | 김 집사 | junior_to_senior_Hunter | Senior | deferential | After learning that Butler Kim trained at the same Nonsan regiment and battalion, Taekyung addresses him as 선배님. |
| 김 집사 | 최 팀장 | butler_to_employer | Young Master | deferential | Butler Kim addresses Choi as 도련님 when agreeing to follow his decision about Guild titles. |
| 임창수 | 혜린 | sponsor_to_sponsored_lover | Hye-rin | condescending-casual | Changsoo refers to himself as this oppa while claiming he will protect her. |
| 최 팀장 | 임꺽정 | guild_team_leader_to_guild_member | Hunter Im | formal-polite | Choi addresses Kkeokjeong as 임 헌터님 while telling him to put on the equipment. |
| 임창수 | 진태경 | rival_guild_team_leader_to_guild_member | Mr. Jang Taekyung | mock-formal and condescending | Changsoo deliberately uses the wrong surname, then dismisses whether Taekyung is Jin or Jang. |
| 진태경 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo | insulting-casual | Taekyung’s retaliatory surname pun after Changsoo misnames him. |
| 임창수 | 송송이 | rival_guild_team_leader_to_guild_member | Miss Song | mock-polite | Uses 송송이 씨 while proposing that Song Song join Sangdong Guild. |
| 송송이 | 임창수 | guild_member_to_rival_guild_team_leader | Shit Changsoo—no, Im Changsoo | blunt but polite | Insults Changsoo with 씹창 and then corrects herself to his proper name while rejecting him. |
| 송송이 | 김 집사 | guild_member_to_guild_master | Guild Master | formal-polite | Requests the Guild Master’s permission before changing Guilds under the wager. |
| 송송이 | 최 팀장 | guild_member_to_team_leader | Team Leader | formal-polite | Asks Choi whether he accepts her possible Guild transfer if the bet is lost. |
| 송송이 | 임꺽정 | younger_guild_member_to_older_guild_member | Uncle | casual-polite | Song Song uses 아저씨 while asking Im Kkeokjeong to agree that Changsoo is nasty. |
| 김 집사 | 임창수 | guild_master_to_rival_guild_member | Changsoo | mock-polite | Butler Kim uses 창수 씨 while accusing Changsoo of refusing to pay. |
| 지점장 | 임춘수 | bank_branch_manager_to_guild_master | Guild Master | formal-deferential | The K Bank branch manager addresses Im Chunsoo as 길드장님 while reporting Changsoo's transfer. |
| 임춘수 | 임창수 | father_to_son | Changsoo | furious-parental | Im Chunsoo uses Changsoo's name alongside hostile forms such as that bastard and you little shit. |
| 하연 | 진태경 | younger_sister_to_older_brother | oppa | casual-familiar; pleading for important requests | Hayeon habitually puts 오빠 first when making an important request. |
| 김정희 | 사장님 | employee_to_restaurant_owner | Boss | formal-polite, becoming firm | Uses the owner's title while demanding an apology and defending Taekyung. |
| 사장님 | 김정희 | restaurant_owner_to_employee | Ajumma | condescending-casual | Repeatedly uses 아줌마 while berating Kim Jeonghee. |
| 진태경 | 김정희 | son_to_mother | Mom | casual-familiar and affectionate | Taekyung's first words after entering the restaurant and seeing his mother. |
| 김정희 | 진태경 | mother_to_son | Son | affectionate-familiar | Calls Taekyung 아들 when surprised by his visit and later asks whether he has eaten. |
| 진태경 | 사장님 | visitor_to_restaurant_owner | Boss | polite but sarcastic | Maintains a superficially respectful address while baiting the owner during the confrontation. |
| 사장님 | 진태경 | restaurant_owner_to_employee_son | you / you little punk | condescending-aggressive | Uses hostile informal forms while trying to intimidate Taekyung. |
| 부동산 아저씨 | 진태경 | real_estate_agent_to_customer | Boss | polite and sales-friendly | The unnamed real estate agent repeatedly addresses Taekyung as 사장님 while arranging a house viewing. |
| 여자 친구 | 박지훈 | girlfriend_to_boyfriend | Oppa | casual-familiar | Jihoon's girlfriend addresses him as 오빠 while asking him to return to the car. |
| 임춘수 | 1팀장 | guild_master_to_team_leader | Team 1 Leader | blunt-commanding | Chunsoo addresses him with a rough 야 while issuing orders and demanding his candid assessment. |
| 1팀장 | 임춘수 | guild_team_leader_to_guild_master | Guild Master | formal-deferential | The Team 1 Leader consistently addresses Chunsoo as 길드장님 while reporting and accepting orders. |
| 진태경 | 하연 | older_brother_to_younger_sister | Sis | casual-familiar | Taekyung addresses Hayeon as 동생아 during their fly investigation. |
| 동료 | 김준수 | Security Team colleague | Junsu | casual-collegial | Uses 준수야 while checking whether Junsu pulled an all-nighter. |
| 보안팀장 | 김준수 | team_leader_to_subordinate | Kim Junsu | blunt-commanding | Shouts 김준수 when the target begins moving. |
| 김권동 | 보안팀장 | subordinate_to_team_leader | Team Leader | deferential | Uses 팀장님 over the radio while reporting on the disguised approach. |
| 보안팀장 | 1번 | supervisor_to_surveillance_agent | Number One | command-radio | Uses the operative’s radio call sign while directing the real-estate-office surveillance. |
| 보안팀장 | 2번 | supervisor_to_surveillance_agent | Number Two | command-radio | Uses the operative’s radio call sign while ordering continued observation. |
| 부동산 아줌마 | 진태경 | real_estate_agent_to_customer | Boss; young bachelor | chatty-polite and flirtatious | The agent calls Taekyung 사장님 and 총각 while offering listings and commenting on his appearance. |
| 김권동 | 진태경 | surveillance_hunter_to_target | young man | friendly and polite | Gwondong maintains his ordinary-neighbor disguise and addresses Taekyung as a younger local acquaintance. |
| 진하연 | 여름이 | caretaker_to_kitten | Yeoreum | affectionate-casual | Hayeon repeatedly calls the kitten by name and refers to herself as Sis. |
| 김권동 | 김준수 | Security Team colleagues | Junsu | casual-collegial | Gwondong uses 진수야 while questioning Junsu’s interpretation of the item. |
| 보안팀장 | 김권동 | team_leader_to_subordinate | Gwondong | blunt-commanding | Uses 권동아 while directing the operation. |
| 진태경 | 최병일 | target_to_attacking_team_leader | Mr. Choi Byungil | mock-polite and taunting | Uses 최병일 씨 while baiting and confronting him. |
| 진태경 | 김준수 | target_to_surveillance mage | Junsu | casual and taunting | Uses 준수야 while questioning him. |
| 임춘수 | 진태경 | guild_master_to_younger_rival | you | blunt-but-familiar | Repeatedly uses 자네 while challenging and testing Taekyung. |
| 김화종 | 임춘수 | familiar_mage_to_guild_master | Chunsoo | gentle-and-familiar | Addresses Im Chunsoo as 춘수 on arriving at the hiking-trail entrance. |
| 임춘수 | 김화종 | former_trainee_to_former_instructor | Instructor | deferential and fearful | Im Chunsoo addresses Hwajong as 교관님 after recognizing his former instructor. |
| 김화종 | 진태경 | senior_Hunter_to_younger_Hunter | Mr. Jin | formal-polite | Hwajong addresses Taekyung as 진태경 씨 while proposing an exchange of stories. |
| 1팀장 | 보안팀장 | guild_team_leader_to_security_team_leader | Security Team Leader | formal-commanding | Team Leader 1 directly addresses the Security Team Leader while warning him about discipline. |
| 보안팀장 | 1팀장 | security_team_leader_to_guild_team_leader | Team Leader 1 | formal-deferential | The Security Team Leader addresses Team Leader 1 as 팀장님 while reporting what he heard. |
| 진태경 | 기사님 | customer_to_moving_driver | Driver | polite | Taekyung addresses the private moving-truck driver by his occupational title on the phone. |
| 이삿짐 아저씨 | 진태경 | moving_driver_to_customer | Mr. Jin Taekyung; Boss | friendly-polite | The driver uses 진태경 씨 on the phone and 사장님 while insisting on moving the capsule. |
| 진무경 | 혁무진 | senior martial artist to subordinate | Hyung Mujin | blunt-senior | Mukyung deliberately misnames Hyuk Mujin as 형무진 before ordering him to stop the carriage. |
| 혁무진 | 진무경 | subordinate to Second Young Master | Second Young Master | deferential | Uses 이공자님 while correcting Mukyung's deliberate misnaming and accepting his orders. |
| 월화 | 진태경 | Lower District Sect branch leader to Jin Family young master | Young Master Jin; our Young Master | polite and lightly playful | Uses 우리 공자님, 진 공자, and the teasing 잠룡 공자 while greeting and teasing Taekyung. |
| 월화 | 혁무진 | inn proprietress and branch leader to visiting martial artist | Young Martial Artist; Martial Artist | polite and teasing | Uses 젊은 무사님 and 무사님 while discussing her profession and correcting Mujin's conduct. |
| 혁무진 | 월화 | Jin Family retainer to Lower District Sect Branch Leader | Young Lady; Branch Leader | formal-polite, then deferential | Initially addresses Wolhwa as 소저, then corrects himself to 지부장님 after learning her identity. |
| 월화 | 진무경 | Lower District Sect Branch Leader and inn proprietress to Jin Family Second Young Master | Young Hero Jin | polite and lightly playful | At departure, Wolhwa addresses Mukyung as 진 소협 after agreeing to accompany the group. |
| 오색귀 | 진태경 | former_bandit_associates_to_prior_benefactor | Boss | pleading and deferential | The Five-Colored Ghosts repeatedly call Taekyung 대형 while begging him to rescue them. |
| 월화 | 춘삼 | Lower District Sect branch leader to subordinate | Chunsam | commanding-familiar | Uses 춘삼아 while directing him to execute the interrogation order. |
| 마적 | 풍양 | mounted-bandit subordinate to bandit leader | Leader | deferential | Uses 단주 when reporting to Pung Yang. |
| 소월 | 철무백 | niece_to_paternal_uncle | Uncle Cheol | familiar-polite | Lee Seowol asks Cheol Mubaek to suppress his heat because she cannot breathe. |
| 철무백 | 소월 | paternal_uncle_to_niece | Seowol | affectionate-familiar | Cheol Mubaek speaks gently to Seowol and says protecting her is his duty. |
| 소월 | 철검대주 | sect_leader_to_subordinate | Iron Sword Squad Leader | formal-commanding | Lee Seowol addresses him while issuing her final instruction about her title. |
| 소월 | 수문각주 | sect_leader_to_subordinate | Master of the Gatekeeper Pavilion | formal-commanding | Lee Seowol addresses him while asserting her authority as Sect Leader. |
| 사자 | 이소월 | enemy_envoy_to_sect_leader | Sect Leader | mock-formal | The Red Wind Band envoy addresses Lee Seowol as 문주님 while delivering the coercive marriage-or-destruction ultimatum. |
| 풍양 | 철무백 | junior_to_older_martial_peer | Senior Cheol | polite and taunting | Pung Yang repeatedly addresses Cheol as 철 선배 while provoking him. |
| 진태경 | 철무백 | junior_to_respected_Peak_master | Sir | apologetic-polite | Taekyung first calls Cheol Grandpa, then corrects himself to the respectful 대협. |
| 월화 | 철무백 | ally_to_injured_master | Sir Cheol | polite and reassuring | Wolhwa addresses the critically wounded Cheol while administering temporary medicine and asking about his attacker. |
| 진무경 | 풍양 | challenger_to_bandit_leader | Pung Yang | challenge-shout | Mukyung calls out Pung Yang by name to begin the confrontation. |
| 풍양 | 이소월 | captor_to_coerced_bride | Young Lady | polite and coercive | Pung Yang addresses Seowol as 소저 while threatening her subordinates and demanding marriage. |
| 풍양 | 진무경 | enemy_to_enemy | you / little brat | condescending and taunting | Uses 네놈 and 어린놈 while threatening to sever Mukyung's limbs. |
| 진태경 | 풍양 | enemy_to_enemy | you pill-popping bastard | insulting-casual | Taekyung openly insults Pung Yang while announcing that he will use a pill too. |
| 풍양 | 진태경 | enemy_to_enemy | little brat; wet-behind-the-ears fledgling | condescending and taunting | Pung Yang dismisses Taekyung as an inexperienced child while challenging his ability to intervene. |
| 무인 | 이소월 | sect_subordinate_to_sect_leader | Sect Leader | formal-deferential | Surviving Mount Heng martial artists address Seowol by her title during the casualty search. |
| 이소월 | 진태경 | rescued_sect_leader_to_benefactor | Benefactor | deferential | Lee Seowol repeatedly addresses Taekyung as 은공 after acknowledging that he and Jin Mukyung saved the Mount Heng Sword Sect. |
| 월화 | 혼주지부장 | chief_branch_leader_to_subordinate_branch_leader | Honju Branch Leader | formal-commanding | Wolhwa addresses him by branch title while directing rumor operations. |
| 진무경 | 이소월 | junior_to_sect_leader | Sect Leader | formal-polite | Uses 문주 while greeting Lee Seowol. |
| 혁무진 | 이소월 | subordinate_to_sect_leader | Sect Leader | deferential and exuberant | Formally praises the Sect Leader while greeting her. |
| 혁무진 | 철무백 | junior_to_respected_Peak_master | Great Hero Cheol | deferential | Begins a formal greeting with 철무백 대협 before being stopped. |
| 철무백 | 진무경 | senior_martial_peer_to_younger_martial_artist | Heaven Shaking Sword | affectionate-teasing | Uses 우리 진천검 while warmly inviting Mukyung to return. |
| 철무백 | 진태경 | senior_martial_peer_to_benefactor | you | casual-teasing | Uses 자네 while teasing Taekyung about his greeting and injuries. |
| 진위경 | 위팽 | lord_to_personal_guard | you | formal-but-familiar | Uses 자네 while assigning Wipeng the banner-preparation task. |
| 하오문도 | 진위경 | informant_to_lesser_family_head | Lesser Family Head | deferential | Uses 소가주님 while correcting Wikyung's misunderstanding about Mukyung's condition. |
| 현령 | 진태경 | county_official_to_celebrated_martial_artist | Great Hero Jin | formal-polite and admiring | Uses 진 대협 while praising Taekyung's alleged exploits. |
| 진태경 | 현령 | martial_artist_to_county_official | County Magistrate | polite and lightly sarcastic | Uses 현령님 while explaining that the Lesser Family Head cannot receive visitors. |
| 혁무진 | 진위경 | Jin Family subordinate to Lesser Family Head | Lesser Family Head | deferential | Uses 소가주님 while confessing that he accepted Taekyung's invitation. |
| 진위경 | 혁무진 | Lesser Family Head to direct family subordinate | you | formal-but-familiar | Uses 자네 while recognizing Mujin and instructing him to keep helping Taekyung. |
| 현령 | 진위경 | county_official_to_lesser_family_head | Lesser Family Head | formal-polite and deferential | Uses 진 소가주님 when asking Taekyung to convey his regards. |
| 현령 | 진무경 | county_official_to_renowned_martial_artist | Heaven Shaking Sword | formal-polite and respectful | Uses 진천검 when asking Taekyung to convey his regards. |
| 동료 쟁자수 | 석칠 | junior_colleague_to_senior_colleague | Hyung | casual-but-respectful | Calls Seokchil 형님 while inviting him to the fire and restraining him. |
| 석칠 | 동료 쟁자수 | senior_colleague_to_junior_colleague | Brat | gruff-casual | Uses 이놈아 while bantering with his fellow porter. |
| 동료 쟁자수 | 청풍 | senior_colleague_to_newcomer | Rookie | casual | Calls Cheongpung 신참. |
| 혁무진 | 아주머니 | childhood_benefactor_to_former_child | Auntie | deferential-polite | Mujin respectfully addresses the local snack-stall vendor who secretly gave him candied hawthorn when he was a child. |
| 청풍 | 진태경 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung repeatedly addresses Taekyung as 은인 after receiving food. |
| 청풍 | 혁무진 | newly met beneficiary to benefactor | Benefactor | deferential | Cheongpung includes Mujin among his 은인들 after receiving the skewers. |
| 혁무진 | 청풍 | martial artist to young master | Young Master | formal-deferential | Mujin uses 공자께서는 when asking why Cheongpung descended from the mountain. |
| 우진태 | 황 소저 | host_to_five_gates_scion | Young Lady Hwang | polite and flirtatious | Woo Jintae presents Shu brocade as a gift while implying personal feelings, then retreats behind a joke. |
| 우진태 | 혁 아우 | older_friendly_sc ion_to_younger_sc ion | Little Brother Hyuk | familiar and patronizing | Woo Jintae promises the male scion an especially impressive gift. |
| 혁 아우 | 우진태 | younger_sc ion_to_older_friendly_sc ion | hyung | familiar and deferential | The scion calls Woo Jintae hyung after they have become close enough to use fraternal terms. |
| 진태경 | 진태 | stranger_to_mocked_First_Rate_sc ion | Jintae | insulting-casual | Taekyung identifies Jintae as the last name in the group and addresses him while challenging the group's spokesman. |
| 진태경 | 우진태 | enemy_to_enemy | you / you bastard | insulting-casual | Taekyung repeatedly addresses Woo Jintae with hostile informal forms while demanding an apology and slapping him. |
| 우진태 | 진태경 | enemy_to_enemy | you / little bastard | condescending and enraged | Woo Jintae uses hostile forms such as 네놈, 애새끼, and 어린놈 while trying to intimidate Taekyung. |
| 갈 소협 | 정 소협 | fellow_Five_Gates_heir | Young Hero Jeong | formal-polite | The unnamed heir addresses the other injured heir by surname and honorific. |
| 정 소협 | 갈 소협 | fellow_Five_Gates_heir | Young Hero Gal | formal-polite | The unnamed heir responds using the other injured heir's surname and honorific. |
| 관리 | 진태경 | official_to_young_martial_artist | Young Master | formal-polite | The official addresses Taekyung as 공자 while explaining the consequences of Prince Shangshan's displeasure. |
| 홍 내관 | 이풍 | political_rivals | Assistant Commissioner Li | mock-friendly and probing | Uses 우리 이 첨사 and a superficially familiar tone while testing and provoking Li Feng. |
| 이풍 | 홍 내관 | political_rivals | Eunuch Hong / Deputy Military Commissioner | formal but sarcastic | Alternates between the official title and Eunuch Hong to mock his demand for familiarity. |
| 공일혁 | 이풍 | martial_rivals | Li Feng of Huashan | casual and taunting | Mocks Li Feng's office and recalls his defeat at Huashan ten years earlier. |
| 이풍 | 공일혁 | martial_rivals | you bastard | hostile and furious | Responds to Gong Ilhyuk's insult toward Huashan with an openly aggressive form. |
| 진태경 | 청풍 | companion_to_young_martial_artist | Young Master Cheongpung | formal-polite | Taekyung uses 청 공자 while correcting Cheongpung's royal-etiquette mistake. |
| 공일혁 | 진태경 | senior_martial_artist_to_junior_martial_artist | Junior | condescending and dismissive | Uses 후배님 while ordering Taekyung to move aside. |
| 진태경 | 공일혁 | junior_martial_artist_to_senior_martial_artist | Senior | polite but firm | Uses 선배님 while intervening on Cheongpung's behalf. |
| 공일혁 | 청풍 | senior_martial_artist_to_junior_martial_artist | Junior | impatient and condescending | Treats Cheongpung as a junior while demanding his introduction. |
| 청풍 | 공일혁 | junior_martial_artist_to_senior_martial_artist | Senior | deferential and apologetic | Uses 선배님 while apologizing for catching Ilhyuk's wrist. |
| 이풍 | 진태경 | senior_official_to_respected_young_martial_artist | Young Hero Jin | formal and respectful | Addresses Taekyung as 진 소협 after praising his reputation. |
| 공일혁 | 홍진 | junior_official_guest_to_senior_official | Deputy Military Commissioner | formal and deferential | Appeals to Hong Jin for his view on the impending disturbance. |
| 이풍 | 청풍 | Huashan lay disciple to martial uncle | Young Hero; Martial Uncle Cheongpung | formal and reverent | Li Feng initially addresses Cheongpung as 소협 while testing his knowledge, then recognizes him as 사숙 after witnessing his Huashan sword technique. |
| 홍진 | 공일혁 | political_host_to_guest | Great Hero Gong | polite but cutting | Hong Jin uses the respectful title while dismissing Gong Ilhyuk and exposing his poor judgment. |
| 청풍 | 이풍 | Martial Uncle to Martial Nephew | Martial Nephew Li Feng | exuberant and deferential | Cheongpung adopts the address to obtain royal-guard armor and weapons. |
| 홍진 | 주표 | servant and political aide to prince | His Highness | formal-deferential | Uses the elongated royal call 전하 while summoning Zhu Bao. |
| 진태경 | 주표 | visitor to prince | His Highness, Prince Shangshan | formal-deferential | Addresses Zhu Bao as 상산왕 전하 after kneeling to meet his gaze. |
| 주표 | 진태경 | prince to visiting young hero | Jin Taekyung | formal and inquisitive | Uses the formal second-person address before asking Taekyung's name and requesting an autograph. |
| 홍진 | 진태경 | political_host_to_young_martial_artist | Young Hero Jin; Young Master Jin; Sleeping Dragon of Shanxi | polite, coaxing, and probing | Uses respectful forms while steering Taekyung toward relaying the Escort Bureau proposal and teasing him with the Seongun Escort Bureau. |
| 진태경 | 홍진 | young_martial_artist_to_political_official | Comrade Chairman—no, Deputy Military Commissioner | casual and teasing, then formally corrective | Deliberately jokes with an inappropriate title before correcting himself to Hong Jin's official office. |
| 진태경 | 이풍 | junior_to_respected_official_and_martial_ally | Great Hero Li | polite and respectful | Agrees with Li Feng's proposal that Zhu Bao visit the Jin Family's banquet. |
| 이풍 | 주표 | official_to_prince | Your Highness | formal-deferential | Suggests that Zhu Bao visit the Jin Family's grand banquet in fifteen days. |
| 주표 | 청풍 | prince_to_young_martial_artist | you | formal and gatekeeping | Refuses Cheongpung's autograph until he acquires a martial title. |
| 홍진 | 청풍 | political_official_to_young_martial_artist | Young Master | formal and curious | Uses 공자께서는 while asking whether Cheongpung has always lived on Huashan. |
| 전령 | 진위경 | military messenger to Lesser Family Head | Lesser Family Head | formal-polite and deferential | Uses 소가주님 when confirming Wikyung's identity. |
| 위팽 | 진무경 | Jin Family retainer to Second Young Master | Second Young Master | deferential and blunt | Uses 이공자 while directing Mukyung to wash before the guest's arrival. |
| 진위경 | 홍진 | political_host_to_deputy_military_commissioner | Comrade Hong | formal-polite and playful | Jin Wikyung adopts Hong Jin's requested casual address, 홍 동지. |
| 홍진 | 진위경 | deputy_military_commissioner_to_lesser_family_head | Lesser Family Head Jin | formal and teasing | Hong Jin addresses Jin Wikyung as 진 소가주님 while flattering and joking with him. |
| 청풍 | 진무경 | young_martial_artist_to_renowned_senior_martial_artist | Young Hero Jin Mukyung | deferential and excited | Cheongpung calls him 진천검 진무경 소협 and later 진 소협 while seeking his duel. |
| 진무경 | 청풍 | senior_martial_artist_to_newly_met_young_martial_artist | Young Hero | deferential and expectant | Mukyung addresses Cheongpung as 소협 while asking whether Great Hero Mae descended from Huashan. |
| 철우 | 백무성 | junior_disciple_to_senior_brother | Senior Brother | deferential | Uses 대사형 while answering Baek Museong. |
| 은향 | 백무성 | junior_disciple_to_senior_brother | Big Brother; Senior Brother | familiar and casual-polite | Repeatedly calls him 큰 오라버니 even after he insists on 대사형. |
| 홍가 | 장칠득 | older_martial_artist_to_junior_martial_artist | Little Brother Jang | familiar and casual | Hong calls Childeuk 장 아우 after inviting him to address Hong as hyung. |
| 장칠득 | 홍가 | junior_martial_artist_to_older_martial_artist | hyung | deferential, then familiar | Childeuk initially uses Senior and then adopts Hong's requested 형님 address. |
| 장칠득 | 진태경 | servant_to_third_young_master | Third Young Master | formal-deferential | Jang Childeuk addresses Taekyung as 삼공자님 while asking permission to report the dangerous training. |
| 유생 | 진위경 | scholar_to_lesser_family_head | Lesser Family Head | formal-deferential | The scholar reports matters to Jin Wikyung and apologizes for his inadequate proposal. |
| 진위경 | 유생 | lesser_family_head_to_scholar | you | formal-but-familiar | Jin Wikyung uses 자네 while correcting and instructing the inexperienced scholar. |
| 위팽 | 유생 | senior_retainer_to_scholar | you | familiar and probing | Wipeng uses 자네 while asking the scholar for his assessment. |
| 매종학 | 청풍 | grandfather_to_grandson | Pung | affectionate-instructional | Mae Jonghak calls young Cheongpung 풍아 while teaching him the Crouching Tiger Fist. |
| 테무르 | 칭겐 | fellow_chieftain | Chinggen | familiar and argumentative | Temur addresses his fellow chieftain by name while defending their khan lineage. |
| 칭겐 | 테무르 | fellow_chieftain | Temur | familiar and cautioning | Chinggen uses Temur's name while warning him not to act rashly. |
| 테무르 | 인도 | hostile_strangers | you Han Chinese bastard | hostile and contemptuous | Temur insults the seated Han Chinese man before attempting to draw his curved saber. |
| 인도 | 테무르 | intimidating_rival_to_chieftain | friend | cold and taunting | The Human Butcher calls Temur a slow friend after forcing him to sit. |
| 인도 | 흑사 | rival_power_to_rival_power | Black Sand | blunt and familiar | Uses 흑사 while cutting off Black Sand's joking introduction. |
| 흑사 | 인도 | rival_power_to_rival_power | you | playful and taunting | Teases the Human Butcher about being called a butcher without showing fear. |
| 흑사 | 칭겐 | alliance_recruiter_to_recruited_chieftain | Chinggen | lightly teasing and probing | Identifies Chinggen by name while commenting on his composure and perceptiveness. |
| 흑사 | 노인 | subordinate_to_overwhelming_unknown_master | Elder, then big brother; both rejected | deferential and fearful | Black Sand first uses 어르신 and then 형님 while trying to placate the old man; the old man rejects both forms. |
| 위팽 | 진태경 | retainer_to_third_young_master | Third Young Master | formal-polite and admonishing | Uses 삼공자 while warning Taekyung to return by noon and behave respectfully toward Jang Taebo. |
| 장태보 | 항아 | elder_neighbor_to_child | Hanga | familiar and instructive | Calls the neighboring boy by name while correcting his speech and sending him home after dark. |
| 항아 | 장태보 | child_to_elder_neighbor | Grandpa | childlike-familiar | Repeatedly calls Jang Taebo 할부지. |
| 진태경 | 항아 | visiting_adult_to_local_child | little one | friendly and coaxing | Questions Hanga and offers food in exchange for information. |
| 혁무진 | 항아 | visiting_adult_to_local_child | little one | coaxing and encouraging | Questions Hanga with an artificially kind smile and offers two food bundles. |
| 진태경 | 장태보 | younger_visitor_to_elder_master | Elder | polite and persistent | Taekyung repeatedly addresses Jang Taebo as 어르신 while requesting his assistance. |
| 장태보 | 진태경 | elder_master_to_younger_visitor | you | gruff and familiar | Jang Taebo uses 자네 while questioning and dismissing Taekyung. |
| 장태보 | 혁무진 | elder_smith_to_young_martial_artist | you / wet-behind-the-ears brat | gruff and insulting | Insults Mujin after Mujin whispers that Jang is senile. |
| 장태보 | 청풍 | elder_smith_to_young_martial_artist | you / lunatic | gruff and incredulous | Initially treats Cheongpung as a lunatic despite recognizing him as Mae Jonghak's disciple. |
| 장팔 | 노인 | stranger_to_elder | Mountain Spirit, then Elder | deferential and apologetic | Jang-pal initially mistakes the old man for a mountain spirit, then shifts to a respectful elder address. |
| 노인 | 장팔 | strangers | you | gruff and familiar | The old man uses 자네 while questioning Jang-pal and accepting his help. |
| 항아 | 노인 | child_to_elder_stranger | Grandpa | childlike-familiar | Hanga calls the unnamed old man 할부지 after he arrives at her family’s home; this is distinct from her address to Jang Taebo. |
| 적천강 | 장태보 | strangers; visiting elder to local smith | Old Man Jang | blunt and familiar | Uses 장 노인 while confirming Jang Taebo’s identity. |
| 적천강 | 진태경 | overwhelming stranger to interrogated young martial artist | you; you bastard | blunt, threatening, and taunting | Uses 너, 네놈, and 이놈 while demanding Taekyung explain Qi Sense and the System. |
| 진태경 | 적천강 | frightened young martial artist to overwhelming elder | elder | polite and fearful | Uses the honorific 어르신 while explaining that the System may have felt like a cheat. |
| 적천강 | 청풍 | overwhelming_elder_to_young_martial_artist | you / little punk | blunt, amused, and threatening | Jeok Cheongang uses 네, 이놈, and related blunt forms while testing Cheongpung. |
| 청풍 | 적천강 | young_martial_artist_to_overwhelming_elder | Grandpa Jeok | casual-familiar despite deference | Cheongpung uses 적 할아버지 while asking Jeok Cheongang to confirm Taekyung's condition; this is a familial form of address, not literal kinship. |
| 혁무진 | 적천강 | subordinate_to_overwhelming_elder | Great Hero Jeok | deferential and fearful | Mujin uses 적 대협 while reporting Jeok’s orders and Taekyung’s awakening. |
| 적천강 | 혁무진 | overwhelming_elder_to_junior_martial_artist | you stupid fool | blunt and mocking | Jeok calls Mujin a 멍청한 놈 after knocking him down during the attempted escape. |
| 장천 | 적천강 | disciple_to_master | Master | deferential and pleading | Jangcheon repeatedly begs Jeok Cheongang to accept him as his Disciple. |
| 적천강 | 장천 | master_to_disciple | you / fool | blunt and gruff | Jeok rejects Jangcheon’s pleas, questions his choices, and threatens to send him down the mountain. |
| 우황태 | 송 문주 | fellow_Five_Gates_head | Sect Leader Song | sharp and defensive | Uses 송 문주 while defending his need to apologize for Woo Jintae. |
| 우황태 | 태 장주 | fellow_Five_Gates_head | Lord Tae | sharp and defensive | Uses 태 장주 while arguing that retreating would damage the Seongun Escort Bureau's standing. |
| 우황태 | 거한 | insulted_stranger_to_accidental_bystander | you ox-headed bastard | aggressive and insulting | Escalates from demanding an apology to insulting the huge Huashan junior after the dropped pill. |
| 백무성 | 철우 | senior_disciple_to_second_junior_disciple | Second | calm and admonishing | Baek Museong uses 둘째 while ordering Chulwoo to stop and later directs him to find Eunhyang. |
| 진위경 | 백무성 | host_to_visiting_martial_artist | Young Hero Baek | formal-polite | Uses 백 소협 when asking whether anything is wrong. |
| 은향 | 철우 | younger_female_disciple_to_older_fellow_disciple | Senior Brother Chul | familiar and casual-polite | Uses 철 오라버니 while teasing and speaking familiarly to Chulwoo. |
| 우황태 | 철우 | insulted_stranger_to_accidental_bystander | Young Hero Chul; Great Hero Chul | apologetic and pleading | Switches from 철 소협 to 철 대협 while apologizing after Chulwoo mocks him. |
| 철우 | 우황태 | stranger_to_stranger | Brother over there | casual-polite and teasing | Uses 형장 while selecting Woo Hwangtae to guide him to a supposed scenic privy. |
| 철우 | 진태경 | stranger_to_stranger | Brother over there | casual-polite | Uses 형장 when stopping after seeing Taekyung near the mountainside. |
| 위팽 | 철우 | Jin Family retainer to visiting martial artist | Defeated Flower Fist | formal-commanding | Uses Chulwoo's epithet while stopping the fight and rebuking both men for disgracing their schools. |
| 진태경 | 철우 | rival_companions | next mountain man | casual-teasing | Taekyung responds to Chulwoo's insult with a mocking counter-insult. |
| 백무성 | 진태경 | senior_martial_artist_to_younger_martial_artist | Young Hero Jin | formal-polite | Baek Museong agrees with Taekyung while correcting Chulwoo. |
| 백무성 | 청풍 | Martial_Nephew_to_Martial_Uncle | Martial Uncle | formal-deferential | Baek formally identifies himself as Cheongpung's Martial Nephew. |
| 공일혁 | 노호검객 | junior_disciple_to_sect_elder | Elder | deferential | Gong Ilhyuk repeatedly addresses the Roaring Fury Swordsman as 장로님 while steering him toward the Jin Family. |
| 철우 | 청풍 | junior_disciple_to_Martial_Uncle | Martial Uncle | apologetic and deferential | Initially calls Cheongpung Young Hero, then recognizes him and apologizes for failing to recognize the senior sect relation. |
| 위팽 | 청풍 | Jin Family retainer to visiting Huashan martial artist | Young Hero Cheongpung | formal-polite and worried | Uses 청 소협 while warning that Cheongpung's refusal of the Sect Leader's order could strain relations between the Jin Family and Huashan. |
| 공야청 | 진태경 | survivor_guardian_to_benefactor | Young Hero Jin | formal-polite | Gong Yacheong greets Taekyung as 진 소협 after returning to the Jin Family. |
| 소율 | 진태경 | child_survivor_to_benefactor | Uncle | childlike-familiar | Soyul repeatedly calls Taekyung 아저씨 while asking to see him. |
| 청풍 | 백무성 | Martial_Uncle_to_Martial_Nephew | Martial Nephew | affectionate-casual | Cheongpung accepts Baek Museong's apology by calling him 사질. |
| 진태경 | 백무성 | junior_martial_artist_to_Huashan_elite | Young Hero Baek | formal-polite | Taekyung addresses Baek Museong as 백 소협 while asking to change seats. |
| 진위경 | 이소월 | host_to_new_sect_leader | Young Lady | formal-polite | Jin Wikyung addresses Lee Seowol as 소저 before accepting her oath. |
| 이소월 | 진위경 | new_sect_leader_to_lesser_family_head | Lesser Family Head | formal-deferential | Lee Seowol refers to Jin Wikyung as 소가주님 when describing his summons. |
| 철무백 | 진위경 | sect_elder_to_lesser_family_head | Lesser Family Head | formal-deferential | Cheol Mubaek formally greets Jin Wikyung as the Lesser Family Head of the Jin Family of Taiyuan. |
| 무인 | 진위경 | vassal_martial_artist_to_lesser_family_head | Lesser Family Head | formal-deferential | The Mount Heng martial artists greet Jin Wikyung as 소가주님 while pledging loyalty. |
| 진태경 | 이소월 | young_martial_artist_to_allied_sect_leader | Young Lady Lee | formal-polite | Taekyung uses 이 소저 while greeting Seowol at the banquet. |
| 진위경 | 철우 | Jin_Family_host_to_visiting_martial_artist | Defeated Flower Fist | formal-familiar | Wikyung uses Chulwoo's epithet while asking Taekyung why he is acting strangely. |
| 진위경 | 추도환 | banquet_host_to_visiting_challenger | Young Hero Choo | formal-polite | Wikyung uses 추 소협 while accepting Choo Dohwan's request for a duel. |

## Exact glossary matches

| 진태경    | **Jin Taekyung**   |
| 진위경    | **Jin Wikyung**    |
| 이소월    | **Lee Seowol**     |
| 백무성    | **Baek Museong**   |
| 철우     | **Chulwoo**        |
| 은향     | **Eunhyang**       |
| 청풍     | **Cheongpung**     |
| 월화     | **Wolhwa**         |
| 산서잠룡   | **Sleeping Dragon of Shanxi** | Jin Taekyung   |
| 화산파    | **Huashan**                      |
| 절정     | **Peak**          |
| 무공     | **martial arts**                                 | Can mean a specific martial art in context            |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 기세     | **aura** / **momentum**                          | Depends on scene                                      |
| 비무     | **duel** / **spar**                              | Formal non-lethal martial contest                     |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 사부     | **Master**                                   |
| 사형     | **Senior Brother**                           |
| 사제     | **Junior Brother**                           |
| 은인     | **Benefactor**                               |
| 시스템              | **System**                     |
| 상태창              | **Status Window**              |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 칭호               | **Title**                      |
| 등급               | **Grade**                      | System/UI field for quest, item, and martial-art classifications; do not use “Rank” here |
| 아이템              | **Item**                       |
| 체력               | **Stamina**                    |
| 민첩               | **Agility**                    |
| 매력               | **Charm**                      |
| 산서     | **Shanxi**             |
| 화산     | **Huashan**            |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 소협      | **Young Hero**                                                  |
| 공자      | **Young Master**                                                |
| 소저      | **Young Lady**                                                  |
| 진태 | **Jintae** | Level 45 spokesman for the five current Five Gates scions. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 송이 | **Song-i** | Short form used for Song Song; Taekyung's love interest. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 시진 | **shichen** | Traditional time unit of approximately two hours. |
| 고자 | **eunuch** | Castrated man; Hong Jin openly identifies himself by this term. |
| 매화삼절 | **Three Plum Blossom Elites** | Collective title for the current Sect Leader’s three exceptional disciples. |
| 연무장 | **training ground** | Private martial-arts practice area at Taekyung's newly rebuilt pavilion. |
| 복호권 | **Crouching Tiger Fist** | Huashan martial art Cheongpung uses during the spar. |
| 귀환자 | **Returnee** | System Title |
| 승부사 | **Gambler** | System Title |
| 패화권 | **Defeated Flower Fist** | Chulwoo’s epithet. |
| 대연무장 | **Grand Training Ground** | The Jin Family's largest training ground and the site of the grand banquet. |

## Listed compact profiles

### Baek Museong.md

# Baek Museong (백무성)

- **Safe through:** Chapter 188
- **Aliases:** Huashan’s Lone Crane
- **Role:** First-generation disciple of Huashan, first of the Three Plum Blossom Elites, and leader of the effort to return Cheongpung, his Martial Uncle, to Huashan.
- **Personality:** Calm, responsible, principled, and patient, though visibly weary of his junior disciples’ antics.
- **Voice:** Gentle and polite with strangers; measured and stern when correcting junior disciples.
- **Relationships:** The current Huashan Sect Leader is his Master; Chulwoo and Eunhyang are his junior disciples; Cheongpung is his Martial Uncle through Mae Jonghak and the current Sect Leader; he met Cheongpung ten years ago.

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 186
- **Aliases:** None
- **Role:** Mysterious young man encountered at Honghwa Inn; an exceptionally young Peak master whose Level Jin Taekyung cannot determine through Qi Sense; the grandson and disciple of Sword Saint Mae Jonghak, who secretly descended from Huashan to seek out and defeat the Ten Dragons and Phoenixes, beginning with Jin Mukyung; he has no martial title yet, naturally opened his Governor Vessel through enlightenment two years ago, has begun teaching Jin Taekyung and Hyuk Mujin using Mae Jonghak's training method, has now used Sword Energy and the Zaha Divine Technique during his spar with Taekyung, defended Taekyung from Jeok Cheongang with Huashan martial arts, and Prince Shangshan will only accept his autograph after he gains one
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, a deep love of martial arts, and a martial artist's competitive pride; he becomes unsettled when someone copies his martial arts
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak, the Sword Saint, is his grandfather and martial instructor; Cheongpung came to Huashan at about age three or four rather than being born there, lived with Mae Jonghak at a hidden residence, and secretly left Huashan without his grandfather's knowledge to challenge the Ten Dragons and Phoenixes; Baek Museong is his Martial Nephew through the current Huashan Sect Leader, met him ten years ago, and is now leading the effort to return him to Huashan; the current Huashan Sect Leader, the Heavenly Sword True Person, is his eldest Senior Brother by generation and has ordered him to return; Cheongpung never underwent Huashan's initiation ceremony and is technically an outsider; Li Feng is his Martial Nephew within Huashan's hierarchy; calls Jin Taekyung and Hyuk Mujin Benefactors after they feed him and has chosen to remain with Taekyung despite the order

### Chulwoo.md

# Chulwoo (철우)

- **Safe through:** Chapter 188
- **Aliases:** None
- **Role:** Level 95 early-Peak Huashan martial artist, second junior disciple of Baek Museong, second of the Three Plum Blossom Elites, and wielder of the Defeated Flower Fist.
- **Personality:** Blunt, defensive, physically intimidating, short-sighted, quick-tempered, coarse, and unconcerned with personal cleanliness.
- **Voice:** Hearty, casual, and blunt, with crude insults, indignant protests, and a competitive streak when provoked.
- **Relationships:** Baek Museong is his Senior Brother; Eunhyang is his fellow junior disciple and frequent bickering partner; Cheongpung is his Martial Uncle, whom he initially failed to recognize and then apologized to; he serves under Huashan’s Sect Leader; he has fallen intensely in love with the eighteen-year-old Lee Seowol after meeting her and immediately imagines marriage and children; after seeing Taekyung interact with Seowol, he publicly challenged Taekyung to a duel.

### Eunhyang.md

# Eunhyang (은향)

- **Safe through:** Chapter 187
- **Aliases:** None
- **Role:** Young female Huashan martial artist, youngest junior disciple of Baek Museong, member of the Three Plum Blossom Elites, and bearer of the Flower Sword Phoenix epithet.
- **Personality:** Bright, mischievous, playful, sharp-tongued, and willing to justify questionable actions with confident moral reasoning.
- **Voice:** Lively and teasing, with familiar phrasing and a sweet laugh; she prefers calling Baek Museong Big Brother.
- **Relationships:** Baek Museong is her Senior Brother; Chulwoo is her fellow junior disciple and bickering companion; she serves under Huashan’s Sect Leader.

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 188
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; Peak Master with forty-five years of internal energy and the Scorching Yang Qi attribute after fully absorbing the Blazing Flame Divine Pill; possesses Jopil’s Flame Divine Palm manual and Ten-Thousand-Year Cold Iron sword entrusted to him by Jeok Cheongang, which he has been ordered to keep secret; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius; possesses one Temporary Strength Pill in his Inventory and has reserved it for a worst-case, life-threatening contingency; Level 71 with 2,400 Fame (+250) and seventy unassigned stat points; completed the Find the Master Artisan Quest after securing Jang Taebo’s agreement to forge his Ten-Thousand-Year Cold Iron into a spear; can roughly copy observed martial forms and copied the Plum Blossom Fist after three days of sparring with Cheongpung; killed Jin Baekyang, the Blade of Flowers, and was rendered unconscious with an Internal Injury by Jeok Cheongang’s Flame Divine Palm
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; loves Song Song; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect, whose marriage proposal he has decided to reject

### Jin Wikyung.md

# Jin Wikyung (진위경)

- **Safe through:** Chapter 188
- **Aliases:** Junzi Sword
- **Role:** Thirty-five-year-old Lesser Family Head and future Family Head of the Jin Family of Taiyuan; has led the family in place of the absent Family Head for two years and established it as Shanxi Murim's hegemon; is investigating Dark Heaven's apparent attack on Shanxi and has ordered three surviving remnants preserved as evidence
- **Personality:** Calm and authoritative in public; affectionate and protective toward Taekyung beneath a stern mask; accepts responsibility from his subordinates and shows immediate concern for family
- **Voice:** Restrained, formal, and commanding with subordinates; openly affectionate with Taekyung
- **Relationships:** Taekyung’s eldest brother and future Family Head; head of Wipeng; member of the Jin Family

### Jintae.md

# Jintae (진태)

- **Safe through:** Chapter 188
- **Aliases:** None
- **Role:** Level 45 First Rate martial artist among the current Five Gates of Shanxi scions; acts as the group's spokesman at Honghwa Inn.
- **Personality:** Pampered, mocking, and confrontational; responds to Taekyung's challenge with condescension rather than apology.
- **Voice:** Guarded and condescending, beginning with a warning about the group's status.
- **Relationships:** One of the five current Five Gates scions, accompanying Seongryong, Cheonwoo, Myeonghwa, and Sohye.

### Lee Seowol.md

# Lee Seowol (이소월)

- **Safe through:** Chapter 188
- **Aliases:** None
- **Role:** Eighteen-year-old current Sect Leader of the Mount Heng Sword Sect; third child of Lee Cheonbaek and his last surviving descendant; publicly insists on being addressed as Sect Leader rather than Young Lady; survived Pung Yang's attack with twenty-four other identified survivors; regards the Mount Heng Sword Sect as effectively destroyed but vows to preserve it for those who died defending it; offered the sect's territorial rights to the Jin Family of Taiyuan and proposed marriage to Jin Taekyung in exchange for three Peak martial arts; arrived at the Jin Family on New Year's Day, swore loyalty, and led the Mount Heng Sword Sect into vassalage under the Jin Family; still awaits Taekyung's answer
- **Personality:** Cold, commanding, and composed; capable of stopping a fierce confrontation with a calm request
- **Voice:** Clear and cool, gentle with Cheol Mubaek but frost-cold and firm when asserting her authority
- **Relationships:** Daughter of the deceased Lee Cheonbaek; younger sister of the deceased Young Sect Leader, Lee Seogeun, and Lee Seogwang; Cheol Mubaek's niece and protected charge, to whom he entrusted the Shura Annihilating Fist manual; has proposed marriage to Jin Taekyung in exchange for the Blood Wolf Sword Technique, Blood Wolf Footwork, and Shura Annihilating Fist

### Wolhwa.md

# Wolhwa (월화)

- **Safe through:** Chapter 185
- **Aliases:** Eun Sowol (은소월); Wolhwa is the name used at Honghwaru
- **Role:** Shanxi’s foremost information merchant and Level 50 martial artist; Branch Leader of the Lower District Sect’s Shanxi branch with authority to mobilize more than thirty Shanxi branches; formerly posing as a high-ranking courtesan at Honghwaru, a pleasure house in central Taiyuan
- **Personality:** Striking, composed, observant, direct, quietly amused, and capable of ruthless, decisive violence when extracting information; comfortable teasing Taekyung while conducting serious information and negotiation work
- **Voice:** Polite and lightly playful; addresses Taekyung as Young Master Jin and delivers embarrassing observations without raising her voice
- **Relationships:** Knows Taekyung as a Honghwaru regular and the youngest son of the Jin Family; says she likes him, though her sincerity is unclear; has negotiated a mutually beneficial alliance with Jin Wikyung and the Jin Family

## Korean source

```text
＃189화



퀘스트



[한 남자가 있어, 널 너무 사랑한]

여인을 향한 한 남자의 애끓는 마음이 질투와 분노로 표출되었습니다.

그는 당신을 쓰러트림으로써 사랑을 쟁취하고자 합니다.



등급 : 절정

제한 : 진태경

임무 : 비무 승리 (미완료)

보상 : 경험치와 명성

실패 : 칭호, [나약한 수컷] 획득



- 퀘스트를 수락하시겠습니까?

- 퀘스트 거절 시, [나약한 수컷] 칭호가 부여됩니다.



‘와, 거지 같네.’

물론 거절했을 시 받게 될 패널티는 두 배로 더 거지 같을 거다.

‘별수 없지.’

혀를 차며 자리에서 일어난 내게 사람들의 시선이 쏠렸다.

“진 공자!”

“진 공자님.”

“진 소협, 나가실 필요 없습니다.”

“맞아요. 철 오라버니가 미쳤나? 갑자기 왜 저래?”

월화와 이소월, 백무성에 이어 대화 몇 마디 나눠 보지 못한 은향까지. 하나같이 걱정 어린 눈빛을 보낸다.

정작 나는 별생각 없는데.

“괜찮습니다. 한판 시원하게 붙죠, 뭐.”

월화가 한숨을 내쉬었다.

“진 공자, 상대가 누군지 알아요?”

“알죠. 패화권 철우.”

“내 생각엔 아직 모르는 것 같은데. 패화권은 화산파에서도 알아주는 기재예요. 매화삼절이라는 이름이 왜 붙었는지 잘 생각해 봐요.”

“잘 싸우니까 붙었겠죠, 뭐.”

“아니, 그게 아니라……. 후우, 그래요. 난 모르겠다. 알아서 해요.”

월화 아웃.

이어 백무성과 은향이 나섰다.

“결코 진 소협을 과소평가하는 건 아닙니다만, 제 둘째 사제는 뭐랄까. 그…….”

“미친 소예요. 철 오라버니 눈 돌아가면 진짜 괴로울 텐데.”

“은향아!”

“왜요. 틀린 말도 아닌데.”

한 줄로 요약하자면 나 정도로는 철우한테 못 비빈다는 소린데.

‘그건 당신들 생각이고.’

내 생각은 다르다. 자만인지, 자신감인지는 아직 스스로도 잘 모르겠다. 단지…….

‘질 것 같지 않아.’

그런 확신이 든다. 나를 향해 소리치는 저놈을 꺾을 수 있다는 확신이.

“당! 장! 나! 와!”

“지금 간다, 인마.”

대연무장에 운집한 천여 명의 군중들의 시선을 받으며, 나는 철우를 향해 걸음을 옮겼다.



* * *



“비무를 멈춰야 합니다.”

백무성의 말에 진위경이 고개를 저었다.

“내 아우는 이미 패화권의 제의를 수락했소. 비무가 끝나는 건 그 후요.”

“진 대협.”

“무슨 연유에서인지는 모르나 둘 사이에 앙금이 있는 모양이오. 이참에 훌훌 털어 버리는 것도 괜찮지 않겠소?”

속 편해 보이는 진위경의 말에 백무성이 내심 한숨을 내쉬었다.

‘상황을 잘 모르는 건가?’

그의 눈에 비친 철우는 지금 아주 단단히 화가 난 상태였다. 진태경의 사지 몇 군데는 부러트려야 멈출 기세다.

‘좋지 않아.’

이쯤에서 멈춰야 한다. 산서잠룡에 관한 소문은 오는 길에 질리도록 들었지만 자신의 둘째 사제에 비할 바는 아니었다.

패화권, 매화삼절이라는 이름은 단순히 사부의 후광으로 얻은 것이 아니니까.

“크게 다칠 수도 있습니다. 일이 벌어지기 전에 막아야 하지 않겠습니까?”

“누가 말이오?”

“……예?”

“아직 비무는 시작하지도 않았소. 승패도 마찬가지지.”

백무성은 지금껏 자신이 잘못 생각했음을 깨달았다. 진위경은 이 상황을 누구보다 잘 이해하고 있었다.

단, 각자의 전제가 달랐을 뿐이다.

“진 대협. 혹시.”

“맞소.”

진위경이 낮게 웃었다. 그의 시선은 비무대를 향해 걸어가는 아우의 뒷모습에 고정되어 있었다.

“저 아이는 승리할 거요. 언제나 그랬듯이.”

“…….”

백무성은 말문이 막혔다. 산서잠룡이 대단한 기재인 것은 맞지만 경험, 무공, 공력. 그 어느 것에서도 철우를 당해 낼 수는 없다.

어린 시절부터 그를 지켜봐 온 백무성은 단언할 수 있었다.

‘진 소가주가 틀렸다. 산서잠룡은 둘째를 당해 낼 수 없어.’

백무성은 고개를 내저었지만 이미 엎질러진 물이었다. 지금 물러나면 두 문파의 위신(威信)이 땅에 떨어질 것이 분명하다.

‘적절한 때 내가 나서야겠군.’

가라앉은 눈빛으로 비무대를 응시하는 그는 한 가지 사실을 놓쳤다.

와구와구. 쩝쩝.

청풍. 진태경을 은인이라 부르는 그가 일언반구 없이 이 사태를 관망하고 있다는 사실을.



* * *



“와아아아!”

“산서잠룡! 산서잠룡!”

“패화권! 패화권!”

비무대에 오르자마자 곳곳에서 환호성이 터져 나온다. 앞서 다른 도전자들이 등장할 때와는 차원이 다른 호응이었다.

“아, 다들 산서잠룡 아시는구나. 참고로 겁. 나. 셉니다?”

“와아아!”

군중들을 향해 열심히 손을 흔들어 주는 나를 철우가 노려봤다.

“너도 손 좀 흔들어 줘. 팬이 없으면 스타도 없다. 몰라?”

“열심히 흔들어 둬라. 앞으로 석 달은 의방 천장만 바라봐야 할 테니까.”

“이유나 묻자. 왜 나한테 지랄이야?”

“몰라서 묻는 거냐?”

나는 어깨를 으쓱해 보였다.

“혹시 고백하기도 전에 차여서?”

“차이긴 누가!”

철우가 울컥한 얼굴로 외쳤다.

“네 녀석이 훼방만 안 놨어도 이미 아이 셋 낳고 잘 살고 있었을 텐데!”

“……그건 빨라도 너무 빠른 거 아니냐.”

과속도 정도가 있지. 만난 지 반 시진도 안 됐는데 어떻게 결혼하고 애 셋을 낳아.

‘무슨 커맨드 센터여? 인구수 200 금방 채우겠네.’

청풍의 말마따나 기러기가 로켓배송으로 데려다줘도 반나절은 걸릴 거다. 게다가 이쪽은 애가 셋이니까 묶음 배송이다.

“상상의 나래 펼치는 건 좋은데, 난 빼 주라. 이 소저랑은 아무 사이도 아닌데 억울하네.”

“헛소리! 그녀가 너를 바라보는 그 눈빛을 내가 똑똑히 봤다!”

“눈빛? 눈빛이 어땠길래.”

“그건, 그건…… 크흑.”

차마 말을 잇지 못하고 신음을 흘린 철우가 눈을 부릅떴다.

“약속하지. 네 발로 이 자리를 빠져나가는 일은 없을 거다.”

“난 착한 사람이니까 네발로 기어서 나가게 해 줄게.”

“그 잔망스러운 주둥이를 박살 내 주마!”

철우가 포효와 함께 달려들었다.

나는 강맹한 기세로 날아드는 일권을 향해 창대를 휘둘렀다.

후우웅! 쾅!

강렬한 충격과 함께 몸이 주르륵 밀린다. 살과 강철의 충돌이라고는 믿기지 않는 위력.

어느새 놈의 손에는 거무튀튀한 권갑(拳鉀)이 끼워져 있었다.

“아이템 좋아 보인다. 잠깐 확인해 봐도 되냐?”

“놈!”

쐐애애액!

말 그대로 미친 소, 그 자체다.

차이점이 있다면 놈에겐 뿔 대신 주먹이 있고, 그 주먹은 단순하게 공격해 오지 않는다는 점이다.

“흡!”

나는 숨을 멈춤과 동시에 창을 휘둘렀다. 권갑과 창날의 궤도가 맞물리며 불꽃을 토해 냈다.

따다다당!

나는 창의 이점인 거리로, 철우는 타고난 반사 신경과 힘으로 서로를 압박했다.

후욱!

강철 같은 다리가 내 허리를 향해 채찍처럼 휘둘러진다.

덩치에 안 맞게 유연하고도 신속한 움직임. 나는 물러남과 동시에 놈의 목을 향해 창을 찔러 넣었다.

팡! 카가각!

발끝이 허공을 가르고 창날은 권갑에 막혔다. 창날을 움켜쥔 철우가 씩 웃었다.

“잡았다.”

그그극!

동시에 어마어마한 힘이 창을 끌어당겼다. 아마 처음부터 이걸 노린 공격이었을 것이다.

창을 잃은 창수는 눈 뜬 허수아비나 다름없으니까.

물론…….

‘이 정도는 예상했어.’

나는 손아귀에 힘을 풀고 철우를 향해 달려들었다. 득의양양하던 놈의 얼굴에 경악이 서렸다.

자신의 힘을 이기지 못한 양손이 창을 쥔 채로 허공에서 만세를 부르는 중이었다.

“너……!”

“창 내놔.”

콰직!

“커헉!”

뭔가 부러지는 소리가 났다. 무르팍에 안면을 가격당한 철우가 비틀거렸다. 다음은 명치다.

퍽!

“꾸읍!”

급소를 얻어맞은 놈이 창을 떨어트리며 뒷걸음질 쳤다. 그사이 나는 여유롭게 창을 회수했다.

“이 자식이!”

그제야 고통에서 벗어나 겨우 허리를 편 철우를 보자마자 피식 웃음이 나왔다.

“우, 웃어?”

“코피 난다. 너.”

“넌 진짜 죽었…… 뭐? 코피?”

황급히 손등으로 콧잔등을 훔친 녀석의 얼굴이 와락 일그러졌다.

“감히 내 얼굴에 상처를 내?”

“괜찮아. 못생겨서 티도 안 나.”

“못생겼으니 더 문제지! 앞으로 더 못생겨질 것 아니냐!”

“…….”

이 새끼 뭐지. 의외로 본인을 정확히 파악하고 있는데?

“크아아아악!”

울분에 찬 고함을 내지른 철우의 눈빛이 번뜩였다.

“사형을 생각해서 적당한 선에서 끝내려고 했건만…… 안 되겠다.”

“제대로 해봐. 그게 내가 여기 나온 이유니까.”

“그래, 진심으로 상대해 주마.”

그 말을 증명이라도 하듯 철우의 권갑에 희미한 빛이 어른거렸다.

“권기(拳氣)?”

아직 미완성의 단계지만 분명 권기다. 놈의 입가에 흉포한 미소가 떠올랐다.

“후회해도 늦었어.”

쉬이이익! 서걱!

불꽃이 튀며 창날이 싹둑 잘려 나갔다. 전신의 모든 공력을 끌어 올린 놈의 주먹이 흐릿해졌다.

쉭! 쉬쉬쉬쉭!

날카로운 돌풍이 휘몰아쳤다. 놈의 주먹이 일으킨 바람을 향해 창을 휘두를 때마다 길이가 한 뼘씩 줄어들었다.

비록 미완성이지만 유형화된 기의 절삭력은 어마어마했다.

서걱! 서걱! 서걱!

촌각도 안 되는 짧은 시간.

내 손에 들려 있던 철창은 이제 팔뚝 길이의 날카로운 쇠막대에 불과했다.

“젠장. 이제 좀 손에 익었나 싶더니.”

이 정도면 창이 아니라 단소다, 단소. 나는 투덜거리며 강철 단소를 허공에 휘둘렀다.

“아, 갑자기 가벼워지니까 적응 안 되네.”

그런 내 모습이 우스운지 철우가 껄껄 웃었다.

“으하하! 가소로운 놈. 그걸로 뭐 하려고?”

“남이사.”

“벌써 패배를 인정하는 거냐?”

“인정은 무슨. 지긴 누가 져?”

“병장기까지 잃은 놈이 무슨 자신감이지? 사형이나 네 형님이 구해 줄 거라고 생각한다면 오산이다.”

나는 피식 실소를 흘렸다.

“너나 후회하지 마라. 차라리 지금 무승부로 하자고 하면 생각해 볼 수도 있고.”

“뭐? 무승부?”

“그래. 대신 앞으로 이 소저한테 집적거리지 않는다는 조건으로.”

“미친놈.”

“그럼 협상은 결렬이다.”

놈을 향해 뚜벅뚜벅 다가갔다. 이제는 창이라고 부를 수 없는 강철 단소를 건들거리며.

“이리 와. 붙자.”

창수가 권각술의 고수에게 겁 없이 다가간다. 그것도 멀쩡한 병장기조차 없는 몸으로.

이런 내 모습에 대연무장을 둘러싼 군중들이 웅성거렸다.

철우도 희한한 생물을 보는 것처럼 눈살을 찌푸렸다.

“넌 도대체…… 뭐 하는 놈이냐?”

“산서잠룡 진태경. 알잖아.”

“숨겨 둔 한 수를 믿고 까부는 건가?”

“글쎄다.”

“혹시 비겁하게 암수(暗手)를 쓰려는 건 아니겠지?”

암수라. 어떤 의미에서는 그와 비슷할지도 모르겠다.

다른 사람들은 볼 수 없는, 나에게만 허락된 수법이니까.

‘상태창 오픈.’

철우와의 거리 불과 삼십 보. 시스템이 응답했다.

띠링.



상태창



[Lv.71 진태경]

직업 : 절정 고수

명성 : 2500 (+250)

칭호 : 5개 (칭호 효과 적용 중)

- 귀환자 (모든 능력치 +10)

- 산서잠룡 (모든 능력치 +15, 명성 +200)

- 명가의 자제 (모든 능력치 +5, 명성 +50)

- 승부사 (일대일 전투 시 전투 관련 능력치 +10%)

- 중급 수련자 (수련 속도 +20%)

근력 : 255 (+55)체력 : 207 (+50)

민첩 : 250 (+55)지력 : 40 (+30)

매력 : 40 (+30)공력 : 45년

맷집 : 200 (+50)

잔여 포인트 : 70

- [승부사] 효과로 인해 특정 능력치가 일시적으로 상승되어 있습니다.

- 잔여 포인트를 분배하십시오.





승부사 효과. 그리고 절정의 벽을 허물며 얻은 70포인트.

나는 거침없이 발걸음을 내디뎠다. 이십 보 앞, 황당해하는 녀석의 얼굴이 보인다.

“미친놈.”

“그런 소리 많이 들어 봤지.”

열다섯 보. 나는 마음속으로 중얼거렸다.

‘근력에 20포인트 부여.’

솨아아.

보이지 않는 바람과 함께 새로운 힘이 스며든다. 일시적으로 300을 넘긴 근력이 활화산처럼 들끓는다.

‘민첩에 50포인트.’

두 번째 바람, 동시에 다음 순간 내디딘 발걸음이 남의 것처럼 낯설게 느껴진다.

‘이렇게 가벼웠나.’

새로운 세상에 들어온 기분이다.

나는 심호흡했다. 남은 열 보의 거리를 먼저 좁힌 것은 내가 아니라 철우였다.

“젠장, 항복하라니까! 이렇게 된 이상 날 원망하지 마라!”

후우웅!

아는 무공이다. 호랑이를 굴복시킨다 해서 붙여진 이름, 복호권.

복호권의 강맹한 일초가 가슴을 강타하려던 그 순간.

솨아아아.

세 번째 바람이 불었다.

그 바람은 내 발끝에서 시작되어서 손끝에서 끝났다.

“야, 95레벨.”

슥.

뾰족한 강철 단소로 철우의 뒷목을 찔렀다. 나는 어느새 놈의 어깨에 앉아 있었다.

“아무래도 내가, 많이 강해진 모양이다.”
```

## Final English reading copy

```markdown
# Chapter 189

> **System**
>
> **Quest**
>
> **There Is a Man Who Loved You So Much**
>
> A man's burning feelings for a woman have manifested as jealousy and rage.
>
> He seeks to win her love by knocking you down.
>
> **Grade:** Peak
>
> **Restriction:** Jin Taekyung
>
> **Task:** Win the duel (Incomplete)
>
> **Reward:** EXP and Fame
>
> **Failure:** Acquire the Title **Weak Male**
>
> —Would you like to accept the **Quest**?
>
> —If you refuse the **Quest**, the Title **Weak Male** will be granted.

*Wow. That sucks.*

Of course, the penalty for refusing would suck twice as much.

*No choice.*

As I clicked my tongue and rose from my seat, everyone's attention turned toward me.

“Young Master Jin!”

“Young Master Jin.”

“Young Hero Jin, you don't need to go out there.”

“That's right. Has Senior Brother Chul gone crazy? Why is he suddenly acting like that?”

Wolhwa, Lee Seowol, Baek Museong, and even Eunhyang, whom I had barely exchanged a few words with, all looked at me with concern.

I was the only one who didn't think much of it.

“It's fine. Let's have a good, clean match.”

Wolhwa sighed.

“Young Master Jin, do you know who your opponent is?”

“I do. Chulwoo, the Defeated Flower Fist.”

“I don't think you do. The Defeated Flower Fist is a prodigy recognized even within Huashan. Think carefully about why he's called one of the Three Plum Blossom Elites.”

“He probably got the name because he's good at fighting.”

“No, that's not what I meant… Whew. Fine, I give up. Do whatever you want.”

Wolhwa was out.

Baek Museong and Eunhyang stepped forward next.

“I'm not underestimating Young Hero Jin in any way, but my Second Junior Brother is, how should I put it? He’s…”

“He's a mad bull. When Senior Brother Chul loses his temper, it’s going to be really painful.”

“Eunhyang!”

“What? It's not wrong.”

In short, they were saying that someone like me couldn't go toe-to-toe with Chulwoo.

*That's what you think.*

I thought differently. I still wasn't sure whether it was arrogance or confidence. I simply…

*I don't think I'll lose.*

I had that certainty. The certainty that I could defeat that man shouting at me.

“Come! Out! Right! Now!”

“I'm coming, you bastard.”

Under the eyes of more than a thousand people gathered around the Grand Training Ground, I walked toward Chulwoo.

* * *

“We have to stop the duel.”

At Baek Museong's words, Jin Wikyung shook his head.

“My younger brother has already accepted the Defeated Flower Fist's challenge. The duel will end after that.”

“Great Hero Jin.”

“I don't know what happened between them, but it seems there is some bad blood between the two. Wouldn't it be good for them to clear it up while they have the chance?”

Baek Museong inwardly sighed at Jin Wikyung's carefree words.

*Does he not understand the situation?*

To Baek Museong, Chulwoo looked absolutely furious. He seemed ready to break several of Jin Taekyung's limbs before he stopped.

*This is bad.*

They had to stop it here. Baek Museong had heard more than enough rumors about the Sleeping Dragon of Shanxi on the way here, but none of them compared to his Second Junior Brother.

The names Defeated Flower Fist and Three Plum Blossom Elites had not been earned through his Master's reputation alone.

“He could be seriously injured. Shouldn't we stop this before something happens?”

“Who?”

“…Pardon?”

“The duel hasn't even begun yet. Neither has its outcome.”

Baek Museong realized that his understanding had been wrong all along. Jin Wikyung understood the situation better than anyone.

Their assumptions were simply different.

“Great Hero Jin. Could it be…”

“That is correct.”

Jin Wikyung gave a low laugh. His gaze remained fixed on the back of his younger brother as he walked toward the dueling platform.

“That boy will win. Just as he always has.”

“…”

Baek Museong was left speechless. The Sleeping Dragon of Shanxi was undeniably an incredible prodigy, but he could not match Chulwoo in experience, martial arts, or internal energy.

Baek Museong had watched Chulwoo since he was a child. He could state it with certainty.

*The Lesser Family Head is wrong. The Sleeping Dragon of Shanxi can't stand against my Second Junior Brother.*

Baek Museong shook his head, but the water had already been spilled. Backing out now would surely drag the prestige of both sects through the dirt.

*I'll have to step in at the right moment.*

As he watched the dueling platform with sunken eyes, he missed one fact.

Munch, munch. Smack, smack.

Cheongpung—the man who called Jin Taekyung his Benefactor—was silently watching the situation unfold.

* * *

“Waaaaah!”

“Sleeping Dragon of Shanxi! Sleeping Dragon of Shanxi!”

“Defeated Flower Fist! Defeated Flower Fist!”

The moment I stepped onto the dueling platform, cheers erupted from every direction. The response was on an entirely different level from when the other challengers had appeared.

“Oh, so everyone knows the Sleeping Dragon of Shanxi. For the record, he’s scary strong.”

“Waaaaah!”

I waved enthusiastically at the crowd, and Chulwoo glared at me.

“Wave your hand a little, too. There are no stars without fans. Don't you know that?”

“Wave all you want. For the next three months, you'll be staring at the ceiling of a medical clinic.”

“Let me ask you one thing. Why the fuck are you giving me shit?”

“You're asking because you don't know?”

I shrugged.

“Did you get rejected before you could confess?”

“Who got rejected!”

Chulwoo shouted with a flushed face.

“If you hadn't interfered, I would already have three children and be living happily!”

“…Isn't that a little too fast?”

There were limits to speeding things up. We hadn't even known each other for half a shichen. How was he supposed to get married and have three children already?

*What is he, a Command Center? He'll hit a population of two hundred in no time.*

As Cheongpung had said, even if a goose delivered them by rocket delivery, it would take half a day. And in this case, there were three children, so it was a bundle delivery.

“It's fine to spread your imagination's wings, but leave me out of it. I don't have anything to do with this Young Lady, so this is unfair.”

“Nonsense! I saw the look in her eyes when she looked at you!”

“The look in her eyes? What was it like?”

“That… That…”

Unable to continue, Chulwoo groaned and widened his eyes.

“I swear. You won't leave this place on your own two feet.”

“I'm a nice guy, so I'll let you crawl out on all fours.”

“I'll smash that insolent mouth of yours!”

With a roar, Chulwoo charged.

I swung my spear shaft at the punch flying toward me with a fierce aura.

Whoosh! Boom!

The intense impact sent my body sliding backward. The force was unbelievable for a collision between flesh and steel.

By then, a pair of dull-black gauntlets covered his hands.

“Those Items look pretty good. Mind if I take a look for a moment?”

“You bastard!”

Whoosh!

He was a mad bull in every sense of the word.

The only difference was that he had fists instead of horns, and those fists didn't simply attack.

“Hup!”

I held my breath and swung my spear. The gauntlets and spearhead met in their arcs, spitting sparks.

Clang-clang-clang!

I pressured him with the spear's advantage in reach, while Chulwoo pressured me with his natural reflexes and strength.

Whoosh!

A steel-like leg lashed toward my waist like a whip.

His movements were fast and flexible despite his size. I retreated while thrusting my spear toward his neck.

Bang! Krrrck!

His toes cut through empty air, while the spearhead was stopped by his gauntlet. Chulwoo seized the spearhead and grinned.

“Got you.”

Krrrck!

At the same time, an immense force pulled the spear toward him. He had probably been aiming for this from the beginning.

A spearman without his spear was no different from a scarecrow with its eyes open.

Of course…

*I expected this much.*

I relaxed my grip and charged toward Chulwoo. The look of triumph on his face turned to shock.

His own strength had sent both hands flying overhead, the spear still clutched in them as though he were cheering.

“You…!”

“Give me my spear.”

Crack!

“Guh!”

Something broke. Chulwoo staggered after taking a knee to the face. Next came his solar plexus.

Thud!

“Ghn!”

After being struck in a vital spot, he dropped the spear and stumbled backward. I calmly retrieved it in the meantime.

“You bastard!”

The moment I saw Chulwoo finally straighten his back after escaping the pain, I let out a quiet laugh.

“Y-You’re laughing?”

“You have a nosebleed.”

“You’re really dead—what? A nosebleed?”

He hurriedly wiped the bridge of his nose with the back of his hand, and his face twisted in outrage.

“How dare you injure my face?”

“It's fine. You're so ugly that no one can tell.”

“That makes it worse! Won't I become even uglier now?”

“…”

What the hell? Surprisingly, he had an accurate grasp of himself.

“Gaaaaah!”

Chulwoo let out a furious roar, and his eyes flashed.

“I was going to finish this at an appropriate level out of consideration for my Senior Brother, but… Never mind.”

“Do it properly. That's why I came out here.”

“Fine. I'll face you seriously.”

As if to prove his words, a faint light shimmered around Chulwoo's gauntlets.

“Fist qi?”

It was still incomplete, but it was unmistakably fist qi. A vicious smile spread across his lips.

“It's too late to regret it now.”

Whoosh! Slice!

Sparks flew as the spearhead was cleanly severed. Chulwoo's fist, drawing up all the internal energy in his body, blurred.

Swish! Swish-swish-swish!

A sharp whirlwind surged around us. Every time I swung my spear at the wind raised by his fists, the spear grew shorter by a handspan.

Though incomplete, the cutting power of his manifested qi was tremendous.

Slice! Slice! Slice!

In less than the blink of an eye, the steel spear in my hands had been reduced to a sharp metal rod no longer than my forearm.

“Damn. I thought I was finally getting used to it.”

At this point, it wasn't a spear anymore. It was a short flute. A short flute.

Grumbling, I swung the steel flute through the air.

“Oh, it's suddenly so light that I can't adjust.”

Perhaps my appearance looked funny to him, because Chulwoo burst into laughter.

“Ha-ha-ha! Pathetic bastard. What are you planning to do with that?”

“Mind your own business.”

“Are you already admitting defeat?”

“What do you mean, admitting defeat? Who's lost?”

“What kind of confidence does a man who has lost even his weapon have? If you think your Senior Brother or your elder brother will save you, you're mistaken.”

I let out a quiet laugh.

“You'd better not regret this. If you suggested a draw right now, I might even consider it.”

“What? A draw?”

“Yeah. On the condition that you stop hitting on this Young Lady.”

“You're crazy.”

“Then negotiations are over.”

I walked steadily toward him, casually brandishing the steel flute that could no longer be called a spear.

“Come here. Let's fight.”

A spearman was fearlessly approaching a master of fist-and-foot techniques. And he was doing it without even a proper weapon in his hands.

The crowd surrounding the Grand Training Ground began to murmur at the sight.

Chulwoo frowned as if he were looking at some strange creature.

“What the hell are you?”

“Jin Taekyung, the Sleeping Dragon of Shanxi. You know that.”

“Are you acting cocky because you trust in some hidden move?”

“Who knows?”

“You aren't planning to use some underhanded trick, are you?”

An underhanded trick. In a way, it might have been similar.

It was a technique permitted only to me—one no one else could see.

*Status Window Open.*

The distance between Chulwoo and me was only thirty paces. The System responded.

Ding.

> **System**
>
> **Status Window**
>
> **Level 71 Jin Taekyung**
>
> **Class:** Peak Master
>
> **Fame:** 2,500 (+250)
>
> **Titles:** 5 (Title effects active)
>
> - **Returnee** (All stats +10)
>
> - **Sleeping Dragon of Shanxi** (All stats +15, Fame +200)
>
> - **Scion of a Prestigious Family** (All stats +5, Fame +50)
>
> - **Gambler** (Combat-related stats +10% in one-on-one combat)
>
> - **Intermediate Trainee** (Training speed +20%)
>
> **Strength:** 255 (+55)  
> **Stamina:** 207 (+50)
>
> **Agility:** 250 (+55)  
> **Intelligence:** 40 (+30)
>
> **Charm:** 40 (+30)  
> **Internal Energy:** 45 years
>
> **Toughness:** 200 (+50)
>
> **Remaining Points:** 70
>
> - Certain stats have been temporarily increased by the **Gambler** effect.
>
> - Assign the remaining points.

The Gambler effect. And the seventy points I had gained by breaking through the wall of the Peak realm.

I stepped forward without hesitation. Twenty paces away, I could see the bewildered look on his face.

“Crazy bastard.”

“I've heard that a lot.”

Fifteen paces.

I muttered inwardly.

*Assign twenty points to Strength.*

Whoosh.

Along with an invisible wind, new strength seeped into me. My Strength, temporarily exceeding 300, churned like an active volcano.

*Fifty points to Agility.*

A second wind blew. At the same time, the step I took felt unfamiliar, as though it belonged to someone else.

*Was I always this light?*

It felt like I had entered an entirely new world.

I took a deep breath. It was Chulwoo, not me, who first closed the remaining ten paces.

“Damn it, I told you to surrender! Now that it's come to this, don't blame me!”

Whoosh!

I knew this martial art. It was called Crouching Tiger Fist because it was said to subdue tigers.

Just as the fierce first strike of the Crouching Tiger Fist was about to slam into my chest—

Whoosh.

A third wind blew.

It began at my toes and ended at my fingertips.

“Hey, Level 95.”

Swish.

I stabbed the back of Chulwoo's neck with the pointed steel flute.

By then, I was already sitting on his shoulder.

“Looks like I've gotten a lot stronger.”
```
