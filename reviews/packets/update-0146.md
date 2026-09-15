<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0146.txt",
      "sha256": "d14ef290858fdd3371725fe9da7540e50c041c0730c9efc28c5992cad8e75ccc",
      "bytes": 13576
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b83c85af6f2ae226f839eacef3f47eeb9eda35e78b0c2de10b907d6e17c396f7",
      "bytes": 4455
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "796e15444432d75b3dbae1a45178418dbbf70bcbb91833df0e54758f59a7ac1b",
      "bytes": 30889
    },
    {
      "path": "characters/Cheongpung.md",
      "sha256": "b0baba97772856af0cbee05eed814b13990186c8326e7113d4759e342776d035",
      "bytes": 1035
    },
    {
      "path": "characters/Hong Jin.md",
      "sha256": "7b504b3e1d46f047053d91cd43db0435792977112998b14535ebbdd64b0b7197",
      "bytes": 831
    },
    {
      "path": "characters/Li Feng.md",
      "sha256": "12b3ab5923fd29f04c5ec05d79eb2c2cc214788aaf1a730a31c9195f4e5d6846",
      "bytes": 888
    },
    {
      "path": "characters/Prince Shangshan.md",
      "sha256": "f86fc3697c2150f7a03ef755ff35e91902579284d829ee4de09dbaa3b1d87200",
      "bytes": 1019
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "820b75d2e3bb19ad4b7b34583c18061fdd110da2596af20c090aafb5aaca7640",
      "bytes": 27136
    }
  ],
  "estimated_tokens": 25238
}
-->

# Durable State Update — Chapter 146

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 146. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 146. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 146,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 146,
    "continuity_sources": [146],
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
    "The City Lord's luncheon has concluded its attendance requirement; the associated Quest Reward is pending until the luncheon ends.",
    "Zhu Bao is ten years old, has trained in martial arts daily for three years, and is an exceptionally skilled young swordsman personally named Zhu Bao; he admires Jin Taekyung and has been invited to the Jin Family's grand banquet in fifteen days.",
    "Taekyung remains below the Peak realm and cannot use Sword Energy despite defeating Jopil, Jin Baekyang, and Pung Yang.",
    "Hong Jin and Li Feng are pursuing the Shaanxi–Shanxi trade project through Huashan, with Li Feng acting as intermediary and Taekyung relaying the proposal to Jin Wikyung; the Seongun Escort Bureau is the proposed base.",
    "Cheongpung is a twenty-year-old Peak master raised by Mae Jonghak, the Sword Saint, and recognized by Li Feng as his Martial Uncle.",
    "Mae Jonghak remained in deep seclusion at a hidden Huashan residence and had been there at least ten years before the luncheon.",
    "Li Feng left Huashan after becoming discouraged by Cheongpung's extraordinary talent, not because of his defeat by Gong Ilhyuk.",
    "Cheongpung knows several Huashan martial arts and can use the Zaha Divine Technique with potent Extreme Yang internal energy.",
    "Cheongpung's exact parentage and the truth behind his claim that a crane delivered him to Mae Jonghak remain unclear.",
    "The identities of the other two members of the Three Hands of Zhongnan remain unknown.",
    "Hong Jin is a eunuch who has served Prince Shangshan since infancy and is the power behind the Shanxi Provincial Office as Deputy Military Commissioner.",
    "Gong Ilhyuk leaves the luncheon humiliated and vows revenge against those who rejected and insulted him.",
    "Li Feng commands the military's respect, while Hong Jin holds influence over civil officials and servants through fear.",
    "Cheongpung wants to join the royal guard because he admires its black armor and accepted Li Feng's Martial Nephew address in exchange for royal-guard equipment.",
    "The four heirs of the Five Gates of Shanxi excluding the Seongun Escort Bureau are frightened of the Jin Family, Huashan, and the government and are being pressured to support Taekyung's side.",
    "Taekyung threatened to absorb Gopyeong Sect as the Gopyeong Branch of the Jin Family of Taiyuan if its young sect leader refused to cooperate.",
    "Jin Mukyung flatly refused Zhu Bao's autograph request three years earlier; Taekyung now promises to obtain Mukyung's autograph for Zhu Bao at the upcoming banquet.",
    "Cheongpung has no martial title yet, and Zhu Bao will not accept his autograph until he acquires one."
  ],
  "continuity_sources": [
    145
  ],
  "open_questions": [
    "What is Cheongpung's exact parentage, and what did Mae Jonghak mean by saying a crane delivered him?",
    "Why did Mae Jonghak remain hidden at Huashan despite the sect eventually finding his residence?",
    "What are the names and individual identities of the other two members of the Three Hands of Zhongnan?",
    "What is the full title of the wuxia novel beginning with 군림…… that Taekyung read through volume thirty-four?",
    "Was the Emperor's reported suspicion of his younger brother the reason Prince Shangshan was sent to Shanxi, and what danger does the imperial succession pose?",
    "What martial title will Cheongpung eventually acquire?"
  ],
  "safe_through": 145,
  "temporary_decisions": [
    "Render 전하 as “His Highness” as the formal royal address and 왕 as “king” when used literally.",
    "Render 초일류 as “advanced First Rate” and 군문 as “military” when describing an affiliation.",
    "Render 풍운검군 as “Wind-and-Cloud Sword Lord” and 오촌 당숙 as “father's cousin.”",
    "Render 태을미리장 as “Taeeul Miri Palm.”",
    "Render 후배님 and 선배님 as “Junior” and “Senior” in the Gong Ilhyuk exchange.",
    "Render 태사부 as “Grandmaster” and 사숙 as “Martial Uncle” in the Huashan context.",
    "Render 자하신공 as “Zaha Divine Technique”; render 근위대 as “royal guard” and 근위대 갑옷 세트 as “Royal Guard Armor Set.”",
    "Render 고평문 as “Gopyeong Sect,” 고평지부 as “Gopyeong Branch,” and 별호 as “martial title” in this chapter's autograph exchange."
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

## Exact glossary matches

| 무림     | **Murim**          |
| 청풍     | **Cheongpung**     |
| 검성     | **Sword Saint**               | Mae Jonghak    |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 화산파    | **Huashan**                      |
| 산서오문   | **Five Gates of Shanxi**         |
| 절정     | **Peak**          |
| 초절정    | **Supreme Peak**  |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 영약     | **elixir**                                       |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 후기지수   | **young prodigy** / **rising martial artist**    | Contextual, not a title                               |
| 마적     | **mounted bandits**                              |                                                       |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 표국     | **Escort Bureau**                            |
| 제자     | **Disciple**                                 |
| 사숙     | **Martial Uncle**                            |
| 사질     | **Martial Nephew**                           |
| 은인     | **Benefactor**                               |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 화산     | **Huashan**            |
| 본가      | **our family / this family**                                    |
| 대협      | **Great Hero** or **Sir** depending tone                        |
| 공자      | **Young Master**                                                |
| 홍진 | **Hong Jin** | Level 22 man at the City Lord's luncheon; delicate in appearance and voice. |
| 이풍 | **Li Feng** | Shanxi Province's Assistant Military Commissioner; former Huashan lay disciple |
| 상산왕 | **Prince Shangshan** | The City Lord and a member of the imperial family who orders the luncheon. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 검강 | **Sword Force** | Higher manifestation than Sword Energy; Pung Yang's is explicitly imperfect because of insufficient enlightenment. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 산서성 | **Shanxi Province** | Province containing the Lower District Sect branches. |
| 원단 | **New Year's Day** | The day the Mount Heng Sword Sect will visit Taiyuan. |
| 갑자 | **jiazi** | Traditional sixty-year cycle. |
| 황상 | **Emperor** | Address or reference to the reigning Emperor. |
| 성운표국 | **Seongun Escort Bureau** | Escort Bureau in southern Shanxi Province. |
| 홍화객잔 | **Honghwa Inn** | Inn where Taekyung, Mujin, and Cheongpung dine. |
| 정삼품 | **Third-Rank** | Official rank of the unnamed Assistant Military Commissioner. |
| 도지휘첨사 | **Assistant Military Commissioner** | Military office held by the unnamed official responsible for training soldiers. |
| 도지휘동지 | **Deputy Military Commissioner** | Second-rank military office held by Eunuch Hong |
| 도지휘사 | **Military Commissioner** | Provincial military commander's office |
| 전하 | **His Highness** | Formal royal address for the resident prince; the official insists on this form instead of king. |
| 주표 | **Zhu Bao** | Personal name of Prince Shangshan. |
| 근위대 | **royal guard** | Guard unit protecting Prince Shangshan. |

## Listed compact profiles

### Cheongpung.md

# Cheongpung (청풍)

- **Safe through:** Chapter 145
- **Aliases:** None
- **Role:** Mysterious young man encountered at Honghwa Inn; an exceptionally young Peak master whose Level Jin Taekyung cannot determine through Qi Sense; descended from the mountains to test himself against the Ten Dragons and Phoenixes; he has no martial title yet, and Prince Shangshan will only accept his autograph after he gains one
- **Personality:** Affable, dreamy, hazy, and childlike in manner, with innocent curiosity, delight in novel public attention, and a martial artist's competitive pride
- **Voice:** Dreamy and hazy, with innocent, polite phrasing
- **Relationships:** Mae Jonghak, the Sword Saint, is his grandfather and martial instructor; Cheongpung was living with him at a hidden Huashan residence by age ten and learned Huashan martial arts; Li Feng is his Martial Nephew within Huashan's hierarchy; calls Jin Taekyung and Hyuk Mujin Benefactors after they feed him

### Hong Jin.md

# Hong Jin (홍진)

- **Safe through:** Chapter 145
- **Aliases:** None
- **Role:** Level 22 Deputy Military Commissioner of Shanxi Province and a eunuch who has served beside Prince Shangshan since infancy; the power behind the Shanxi Provincial Office and the military's second-ranking official, he manages the City Lord's luncheon and redirects a planned Shaanxi–Shanxi trade project toward Huashan.
- **Personality:** Composed, observant, and socially deft; eases tension by redirecting attention to the arriving guests and flattering Taekyung.
- **Voice:** Delicate, complimentary, and conversational.
- **Relationships:** Recognizes Taekyung as a young hero of the Jin Family of Taiyuan and increasingly enjoys his company and ruthless political methods.

### Li Feng.md

# Li Feng (이풍)

- **Safe through:** Chapter 145
- **Aliases:** None
- **Role:** Assistant Military Commissioner of Shanxi Province; former Huashan lay disciple who left the sect nearly ten years ago
- **Personality:** Resolute, proud, blunt, and hostile toward political and martial rivals
- **Voice:** Formal and restrained in official settings; dry and cutting with opponents
- **Relationships:** Former lay disciple of Huashan; visited the hidden residence of his Grandmaster Mae Jonghak and saw ten-year-old Cheongpung there; recognizes Cheongpung as his Martial Uncle; direct subordinate and political rival of Hong Jin, the Deputy Military Commissioner; agrees to act as Hong Jin's intermediary with Huashan and send a messenger pigeon to his Master; bears a humiliating martial grievance involving Gong Ilhyuk

### Prince Shangshan.md

# Prince Shangshan (상산왕)

- **Safe through:** Chapter 145
- **Aliases:** None
- **Role:** The City Lord and a member of the imperial family; ten-year-old Prince Shangshan, whose personal name is Zhu Bao, is an exceptionally skilled young swordsman who has trained daily for three years.
- **Personality:** Earnest, admiring, and eager to emulate Jin Taekyung; despite his royal dignity, he shows openly childlike enthusiasm for martial arts and Taekyung's reputation.
- **Voice:** Archaic and formal in the manner of a historical drama, with openly eager and childlike reactions beneath his royal diction.
- **Relationships:** Commands the unnamed Third-Rank Assistant Military Commissioner to attend the luncheon and hosts the gathering of young Murim prodigies; admires Jin Taekyung and seeks to emulate him; has been invited to the Jin Family's grand banquet in fifteen days, where Taekyung promises to obtain Jin Mukyung's autograph for him.

## Korean source

```text
＃146화



모든 만남에는 헤어짐이 있는 법.

눈에 익은 육두마차가 가까이 다가오자 주표가 손바닥만 한 뭔가를 내게 내밀었다.

“이게 뭡니까?”

“오늘 만남에 대한 과인의 보답이다.”

“어이쿠, 뭐 이런 걸 다…….”

건네받아 자세히 살펴보니 일종의 황금 메달이다.

표면에 구름과 용이 섬세하게 음각된 그것은 햇빛을 받아 번쩍 빛났다.

띠링.



- 퀘스트 대상이 오늘의 만남을 매우 흡족해합니다!

- 퀘스트 보상으로 [상산왕의 증표]를 얻었습니다!



“과인의 증표다. 혹시 따로 원하는 물건이나 소원이 있다면 증표를 들고 찾아오너라. 내 힘이 닿는 데까지 들어줄 터이니.”

“오.”

교환 쿠폰이네.

중국집 쿠폰은 스무 장에 탕수육 대짜인데, 이건 무려 상산왕의 교환 쿠폰이니까 각종 영약이나 보물로 바꿀 수 있을지도 모르겠다.

‘안 그래도 무기가 하나 필요하긴 한데.’

열화신단을 흡수한 덕분에 공력은 충분한 상황.

다만 쓸 만한 창이 없다는 게 아쉽던 차다. 다른 무기들은 처음부터 거의 일회용 젓가락처럼 쓰고 버리는 수준이었으니까.

‘아예 지금 확 바꿔 버려?’

순간 고민했지만 이내 고개를 저었다.

이미 큰 위기는 넘겼다. 급할 것 없는 상황에 왕의 증표를 무기 하나와 교환하기에는 너무 아깝다.

“감사합니다. 저 이거 되게 갖고 싶었던 건데.”

허리를 꾸벅 숙이자 주표가 까치발을 들고 내 머리를 쓱쓱 쓰다듬었다.

“그대가 좋아하니 나도 기쁘다.”

“…….”

이거 되게 기분 묘하네. 귀여우니까 봐준다.

그사이 우리를 데려다줄 마차가 멈춰 섰다. 마차에 오르려는 내게 주표가 손을 흔든다.

“조심히 가게! 다음에 또 와!”

다음에는 네가 와야지, 인마.

새해 첫날, 그러니까 원단(元旦)까지는 고작 보름 남짓 남았다. 아마 그때쯤 어린 왕을 다시 만날 수 있을 것이다.

“그럼 이만.”

“다녀오겠습니다, 전하.”

마차가 워낙 크다 보니 입구도 넓다. 나와 홍진은 나란히 마차에 올랐다.

“……응?”

아니, 잠깐만. 너무 자연스러워서 넘어갈 뻔했네.

나는 황당한 마음을 담아 홍진을 바라봤다.

“뭡니까?”

“응? 왜요?”

“이거 태원진가 가는 마차인데요.”

“알아요. 그래서 탄 거지.”

“예?”

“쇠뿔도 단김에 빼라고. 이참에 진 소가주님과 이야기를 한번 나눠 봐야 하지 않겠어요?”

빙긋 웃은 홍진이 손가락을 튕기자 관리 한 명이 바람처럼 달려왔다.

“도지휘동지. 분부하실 일이라도?”

“선약도 없이 방문하는데 선물이라도 듬뿍 가져가야지. 미리 전령을 보내서 정중히 인사드리는 것도 잊지 말고.”

“명을 받들겠습니다!”

이풍도 휘하의 장수에게 지시를 내렸다.

“귀빈이시다. 태원진가까지 모셔다드려라.”

“충!”

두 사람의 명령에 자그마치 백 명에 달하는 병력과 급하게 꾸려진 사절단이 일사불란하게 움직이기 시작한다.

그 광경에 뒤따라 오르려던 청풍이 작게 박수를 쳤다.

“우와.”

그토록 염원하던 근위대 굿즈 세트를 손에 넣은 그는 당분간 태원진가에 머무르기로 했다.

이풍이 나를 향해 고개를 까딱 숙였다.

“사숙을 부탁드리겠소.”

“별말씀을.”

그런 말을 굳이 듣지 않아도 이쪽에서 먼저 친하게 지내고 싶은 상대다.

청풍을 징검다리 삼아 화산파와의 관계를 돈독히 한다면 태원진가의 앞날도 화창할 게 분명하니까.

‘재밌는 놈이기도 하고.’

청풍이 해맑게 웃으며 손을 흔들었다.

“이풍 사질, 난 걱정하지 말아요! 진 공자랑 같이 있으면 재미있는 일이 자꾸자꾸 생기거든요!”

“……혹시 싶어서 말해 두는데, 사고만 치지 마십쇼.”

“네!”

대답은 잘한다.

나는 남아 있는 사람들을 향해 고개를 돌렸다.

“너희는 어떻게 하기로 했어?”

산서오문의 후기지수들이 우물쭈물 대답했다.

“원단이 다가올 때까지 홍화객잔에 묵을 계획입니다.”

“본가에 다녀오기에는 워낙 시간이 빡빡하기도 하고…….”

“사실 돌아갈 엄두도 안 납니다.”

“지금 돌아가면 아버지께서 절 죽이실지도 몰라요.”

우울하기 짝이 없는 대답이다.

하긴, 지금쯤이면 전날 있었던 일에 대한 소문이 날개 달린 말처럼 퍼져 나가고 있을 테니 그럴 만도 하다.

나는 녀석들을 보며 혀를 찼다.

“원단까지는 얌전하게 있어라. 문주님들께는 나중에 말 잘해 놓을 테니까.”

“저, 정말이십니까?”

“그 대신 너희도 각자 잘하고. 무슨 얘긴지 알지?”

“성운표국…… 예, 알겠습니다.”

이미 대세는 거스를 수 없다. 이제는 이 녀석들도, 산서오문의 문주들도 그 사실을 알 것이다.

앞으로는 그저 태원진가의 밑에서 최대한 몸집을 불리는 수밖에.

“그래, 그럼 수고들 하고 원단에 보자.”

“네?”

“왜, 뭐.”

“저, 저희도 가는 길인데요.”

“어디. 홍화객잔?”

“예.”

나는 황당해하는 녀석들에게 한마디를 날렸다.

“이거 태원진가 급행이야.”

쾅!

문이 닫히기 무섭게 마차가 움직이기 시작했다.



* * *



여섯 명이 앉아도 넓었던 내부다. 나와 청풍, 그리고 홍진 세 사람은 각자 몇 자리씩을 차지하고 푹신한 좌석에 몸을 기댔다.

“여기서 살아도 될 것 같아요.”

행복한 웃음을 띤 청풍이 말을 이었다.

“할아버지와 살 때는 풀이나 돌 위에서 잤거든요. 이제는 그렇게 못 살 것 같아요.”

문명을 접한 원시인이 따로 없네.

그 말에 홍진이 호기심 어린 눈빛으로 물었다.

“그럼 공자께서는 줄곧 화산에 살았던 건가요?”

“네. 엄청 어릴 때부터요. 하지만 화산에서 태어난 건 아니래요. 예전에 할아버지께 여쭤본 적이 있는데, 화산에 온 건 제가 서너 살 때라고 들었어요.”

그렇겠지. 검성이 아무리 엄청난 고수라지만 육아에는 한계가 있기 마련이다.

초절정 고수가 된다고 남자 가슴에서 젖이 나오지는 않을 테니까.

“…….”

아냐, 초절정 고수라면 혹시 몰라.

검기, 검강도 쓰는 괴물들인데 젖 정도야 나올 수 있지.

나는 호호백발 할아버지가 갓난아기에게 젖을 물리는 장면을 상상해 보았다.

“우웩.”

“은인, 괜찮으세요?”

“진 공자. 괜찮아요?”

“괜찮습니다. 잠깐 속이 메슥거린 것뿐이에요.”

“어머, 그러면 안 되지. 자, 내 무릎에 누워요.”

“…….”

확 그냥 무릎을 부숴 버릴까 보다.

내가 눈으로 쌍욕을 퍼붓자 홍진이 입을 가리며 웃었다.

“호호, 역시 진 공자는 놀리는 재미가 있다니까.”

미인이 저런 말을 했다면 나도 따라서 헤헤 웃었을 텐데, 홍진은 명백한 남자다. 얼굴에 하얗게 분을 칠하고 입술에 뭘 발라도 그 사실은 달라지지 않는다.

‘내관 출신이라고 했지.’

내관이면 내시 아닌가?

예전에 듣기로는 내시라고 해서 꼭 고자는 아니라던데. 하지만 홍진이 달린 놈인지 안 달린 놈인지 구분할 방법이 없다.

“진 공자.”

“예, 예?”

“지금 어디 보고 있어요?”

“아, 뭐가 묻은 것 같아서 그만.”

젠장, 걸렸네.

무림인은 아닌데 눈치가 절정 고수 급이다. 홍진의 하체에서 시선을 뗀 나는 황급히 화제를 돌렸다.

“그런데 이풍 대협은 어쩌다가 군문에 들어가게 된 겁니까?”

“이 첨사? 당연히 무과에 급제해서 들어온 거죠. 그 후로는 쭉 탄탄대로였고.”

“역시 화산파 속가제자라 다르긴 하군요.”

“영향이 없다고는 말 못 하겠지만 꼭 그런 것만은 아니에요. 고작 십 년 만에 정삼품 도지휘첨사가 된다는 건 정말 어려운 일이거든.”

“정삼품이라면……?”

“정삼품이 뭐예요? 먹는 건가?”

높은 직책인 건 대충 알겠는데 딱 거기까지다.

영 감을 못 잡는 나와 청풍에게 홍진이 차근차근 설명해 주었다.

“고위직이죠. 각 성에 겨우 넷밖에 없는 데다가 이 첨사 같은 경우는 품계로 군부에서 세 손가락 안에 들어요.”

홍진이 손가락을 하나씩 꼽았다.

“총사령관인 도지휘사, 그 아래가 나. 그리고 세 번째가 이 첨사. 물론 모두의 위에 계신 분이 상산왕 전하시고.”

“도지휘사요?”

“곧 은퇴를 앞둔 분이죠. 대장군의 아들로 태어나 약간의 공을 세웠고 뇌물을 엄청나게 좋아하시는.”

부패한 군인이군. 생계형 비리가 일상이 되어 버린.

총사령관이라는 인간이 그 모양이니 근래 산서성 치안이 엉망이었던 것도 충분히 설명이 된다.

“지금의 도지휘사는 무능해요. 항산검문이 무너지자마자 마적 떼가 활보하는 것만 봐도 알 수 있죠.”

“그렇게 무능하면 차라리…….”

잘라 버리지 그러십니까, 라는 말을 내뱉기 전에 꿀꺽 삼켰다. 내가 뭐라고 남의 직장 일에 관여를 하나. 그것도 고위 공무원들인데.

이런 내 반응에 홍진이 친절한 설명을 덧붙였다.

“도지휘사는 황상께서 직접 임명하세요. 해임도 마찬가지고.”

“아.”

“뭐, 그래도 그 이상의 욕심은 없으니 다행이죠. 나도 뇌물 좋아하니까 욕할 처지는 아니고.”

뭐 이런 놈이 다 있어.

각종 뇌물 수수 혐의에 결백을 주장하는 정치인들은 TV에서 많이 봤지만 홍진 같은 경우는 처음이다.

“왜요, 내가 그렇게 청렴해 보였나?”

“아뇨. 뇌물 좋아하실 것 같긴 했는데…….”

“이렇게 대놓고 말할 줄 몰랐다?”

“뭐, 그렇죠. 솔직히 지금 살짝 당황했습니다.”

“진 공자. 그거 알아요?”

홍진이 진지한 표정으로 말을 이었다.

“나, 물건이 없어.”

“예?”

“고자라고.”

“…….”

이거 뭐 어떻게 대답해야 하냐. 짐작은 했지만 이런 폭탄 발언을 갑자기 던질 줄이야.

창밖을 구경 중이던 청풍이 궁금한 듯한 얼굴로 대뜸 끼어들었다.

“고자가 뭐예요?”

“……제발, 제발 입 좀 다물어.”

고추가 없다잖아, 고추가!

일분일초가 느릿하다. 나는 식은땀을 흘리며 입을 열었다.

“유감입니다.”

“유감일 것까지야. 살다 보면 없는 사람도 있고, 있는 사람도 있지. 안 그래요?”

“그……렇죠.”

존경스러운 마인드에 괜히 나까지 숙연해진다.

그 와중에 고자의 뜻을 모르는 원시인 놈은 눈치도 없이 자꾸 떠들어 댔다.

“은인, 고자가 뭔지 알려 주시면 안 돼요?”

죽어도 안 알려 줄 거다. 절대.

알려 줘 봤자 ‘와, 저 고추 없는 사람 처음 봐요!’ 이딴 소리 지껄일 확률이 99.99%니까.

하지만 홍진은 의연했다.

“고자는 고추가 없어요.”

“와, 저 고추 없는 사람 처음…….”

“아, 닥치라고!”

헉, 깜짝 놀란 청풍이 헛숨을 들이켰다.

“으, 은인.”

“진정해요. 진 공자. 산에서 살다 왔으면 그럴 수도 있죠. 그리고 뭐, 내가 하루 이틀 고자로 살고 있는 것도 아니고.”

“그래도 말이 너무 심하잖아요.”

“제가 잘못한 거예요? 정말 죄송합니다.”

“괜찮아요. 어깨 펴. 아직 달려 있잖아.”

고자 수십 년 짬밥이 어디 가는 게 아니구나.

진정하라는 듯 손을 내저은 홍진은 대수롭지 않게 말을 이어 갔다.

“내가 내린 결정에 대해서는 후회한 적 없어요. 일가 피붙이가 굶어 죽어 가는 마당에 뭐든 못 하겠어. 안 그래요?”

“암요. 그렇죠.”

“저도, 저도 그랬을 거예요!”

지금은 홍진이 무슨 말을 하든 맞장구쳐 줘야 한다. 나와 청풍은 대역 죄인이 된 기분으로 고개만 끄덕였다.

“난 청렴하진 않지만 신의를 저버릴 만큼 비겁한 놈은 아니에요. 그랬다면 지금까지 전하를 모시지도 않았겠지.”

홍진이 흐릿한 시선으로 창밖을 응시했다.

“오래전 선황(先皇)을 곁에서 모셨었죠. 제게 상산왕 전하를 보필하라는 명을 내리셨어요.”

“선황께서요?”

죽은 전대 황제가 그런 부탁을 했을 정도라면 그때 역시 내관 중에서도 상당한 고위직이었다는 뜻이다.

고개를 끄덕인 홍진이 말을 이었다.

“변방으로 귀양 아닌 귀양을 왔지만…… 지금은 이 정도로 만족해요. 충분히.”

말과는 달리 눈동자에는 숨길 수 없는 빛이 스며들어 있다.

야망? 희망? 그것이 품은 의미를 알아차리기도 전에 빛은 사라졌고, 마부의 조용한 음성이 귓가를 파고들었다.

“태원진가가 보입니다.”
```

## Final English reading copy

```markdown
# Chapter 146

Every meeting must eventually end in a parting.

As the familiar six-horse carriage drew near, Zhu Bao held out something about the size of my palm.

“What is this?”

“My reward for today’s meeting.”

“Oh, you really didn’t have to…”

When I accepted it and examined it closely, I saw that it was a kind of golden medallion.

Clouds and a dragon had been delicately engraved into its surface, which flashed brilliantly in the sunlight.

*Ding.*

> **System**
>
> - The Quest target is extremely pleased with today’s meeting!
>
> - As a Quest Reward, obtained **Prince Shangshan’s Token**!

“It is my token. If there is anything else you desire or a wish you would like granted, bring this token and come find me. I shall fulfill it to the best of my ability.”

“Oh.”

A coupon for an exchange.

At a Chinese restaurant, twenty coupons would get you a large serving of sweet-and-sour pork. Since this was a coupon from Prince Shangshan, I might be able to exchange it for all kinds of elixirs or treasures.

*I do need a weapon, too.*

Thanks to absorbing the Blazing Flame Divine Pill, I had more than enough internal energy.

It was just a shame that I didn’t have a decent spear to use. As for the other weapons, I had used and discarded them from the start like disposable chopsticks.

*Should I just trade it in right now?*

I considered it for a moment, then shook my head.

The greatest dangers had already passed. Exchanging the prince’s token for a single weapon when there was no immediate need would be a waste.

“Thank you. I really wanted something like this.”

When I bowed deeply from the waist, Zhu Bao rose onto his tiptoes and gently ruffled my hair.

“I am happy that you like it.”

“……”

This felt really strange. I’d let it slide because he was cute.

In the meantime, the carriage that would take us home came to a stop. As I was about to climb aboard, Zhu Bao waved at me.

“Take care! Come again!”

*Next time, you should come to me, you little punk.*

There were only a little over two weeks left until New Year’s Day. I would probably be able to see the young prince again around then.

“Then, I shall take my leave.”

“I’ll return, Your Highness.”

The carriage was so large that its entrance was wide as well. Hong Jin and I climbed aboard side by side.

“……Hm?”

Wait a minute. That had been so natural that I’d almost let it pass.

I stared at Hong Jin in disbelief.

“What is it?”

“Hm? Why?”

“This carriage is going to the Jin Family of Taiyuan.”

“I know. That’s why I got on.”

“What?”

“You know what they say—strike while the iron is hot. Shouldn’t I take this opportunity to have a conversation with the Lesser Family Head Jin?”

Hong Jin smiled pleasantly and snapped his fingers. An official came running over like the wind.

“Deputy Military Commissioner. Do you have an order for me?”

“We’re visiting without an appointment, so we should bring plenty of gifts. Don’t forget to send a messenger ahead to offer them our respects.”

“I shall carry out your orders!”

Li Feng also issued an order to one of the officers under his command.

“He is an honored guest. Escort him to the Jin Family of Taiyuan.”

“Yes, sir!”

At the two men’s commands, nearly a hundred soldiers and a hastily assembled delegation began moving in perfect order.

Cheongpung, who had been about to climb aboard after us, gave a small round of applause at the sight.

“Wow.”

Having obtained the royal guard gear set he had longed for so desperately, he decided to stay at the Jin Family of Taiyuan for the time being.

Li Feng dipped his head toward me.

“I entrust Martial Uncle to you.”

“Of course.”

Even without hearing him say that, Cheongpung was someone I wanted to become friends with first.

If I used him as a bridge to strengthen the Jin Family of Taiyuan’s relationship with Huashan, our family’s future would surely be bright.

*He’s an interesting guy, too.*

Cheongpung waved with a sunny smile.

“Martial Nephew Li Feng, don’t worry about me! Interesting things keep happening whenever I’m with Young Master Jin!”

“Just in case, I’ll say this now. Don’t cause any trouble.”

“Yes!”

At least he was good at answering.

I turned toward the people who remained behind.

“What have you decided to do?”

The young prodigies of the Five Gates of Shanxi answered hesitantly.

“We plan to stay at Honghwa Inn until New Year’s Day.”

“It would be difficult to visit our families. There isn’t much time…”

“To be honest, we don’t even dare go back.”

“If I return now, my father might kill me.”

Their answers were as gloomy as could be.

Then again, rumors about what had happened the day before had probably already spread like wildfire, so their fear was understandable.

I clicked my tongue as I looked at them.

“Behave yourselves until New Year’s Day. I’ll smooth things over with the Sect Leaders later.”

“Are you really going to do that?”

“But in return, each of you needs to do your part. You know what I mean, right?”

“The Seongun Escort Bureau… Yes, sir. We understand.”

The tide could no longer be turned. By now, both these young men and the Sect Leaders of the Five Gates of Shanxi would know that.

All that remained was to grow as large as possible under the Jin Family of Taiyuan.

“All right, then. Do your best, and I’ll see you at New Year’s.”

“What?”

“Why? What is it?”

“W-we’re going the same way.”

“Where? To Honghwa Inn?”

“Yes.”

I tossed one final remark at the bewildered young men.

“This is an express carriage to the Jin Family of Taiyuan.”

*Bang!*

The carriage began moving almost as soon as the door slammed shut.

* * *

The inside had been spacious even with six people seated in it. Cheongpung, Hong Jin, and I each claimed several seats and leaned back against the soft cushions.

“I think I could live here.”

Cheongpung continued with a blissful smile.

“When I lived with Grandfather, I slept on grass or rocks. I don’t think I could live like that anymore.”

*He’s a primitive man discovering civilization.*

At his words, Hong Jin asked with curious eyes,

“Then have you always lived on Huashan, Young Master?”

“Yes. Ever since I was very young. But apparently I wasn’t born on Huashan. I asked Grandfather about it once, and he said I came to Huashan when I was three or four years old.”

That figured. No matter how great a master the Sword Saint was, even he had limits when it came to raising a child.

Reaching the Supreme Peak realm wouldn’t make milk come out of a man’s chest, after all.

“……”

*Actually, a Supreme Peak master might be able to do it.*

They were monsters who could use Sword Energy and Sword Force. Producing a little milk couldn’t be beyond them.

I imagined a white-haired old man nursing a newborn baby.

“Ugh.”

“Benefactor, are you all right?”

“Young Master Jin, are you all right?”

“I’m fine. I just felt a little nauseated.”

“Oh my, that won’t do. Here, lie down on my lap.”

“……”

*Maybe I should just smash his knee.*

When I hurled a silent double curse at him with my eyes, Hong Jin covered his mouth and laughed.

“Hoho. As expected, Young Master Jin is so much fun to tease.”

If a beautiful woman had said that, I would have laughed along with her. But Hong Jin was unmistakably a man. No amount of white powder on his face or lipstick on his lips could change that fact.

*He said he used to be a palace attendant.*

Didn’t that make him a eunuch?

I had heard once that not every eunuch was necessarily castrated. But there was no way to tell whether Hong Jin was equipped or not.

“Young Master Jin.”

“Yes, yes?”

“What are you looking at right now?”

“Ah, I thought there was something stuck there.”

*Damn it. He caught me.*

He wasn’t a Murim martial artist, but his ability to read the situation was on the level of a Supreme Peak master. I quickly pulled my gaze away from Hong Jin’s lower body and changed the subject.

“By the way, how did Great Hero Li Feng end up joining the military?”

“Assistant Military Commissioner Li? He passed the military examination, of course. After that, it was smooth sailing all the way.”

“As expected of a Huashan lay disciple.”

“I can’t say that had no influence, but it wasn’t only because of that. Becoming a Third-Rank Assistant Military Commissioner in only ten years is extremely difficult.”

“Third-Rank means…?”

“What is Third-Rank? Is it something you eat?”

I vaguely understood that it was a high position, but that was about it.

Seeing that Cheongpung and I had no idea what he was talking about, Hong Jin explained patiently.

“It’s a high office. There are only four such positions in each province, and in terms of rank, Assistant Military Commissioner Li is one of the top three in the military.”

Hong Jin counted them off on his fingers.

“The Military Commissioner, who is the commander in chief. Then me, directly beneath him. And third is Assistant Military Commissioner Li. Of course, His Highness Prince Shangshan stands above all of us.”

“The Military Commissioner?”

“He’s about to retire. He was born the son of a Grand General, accomplished a little, and has a tremendous fondness for bribes.”

*A corrupt military official. The kind whose petty corruption had become a way of life.*

With the commander in chief being that kind of person, it was easy to understand why security in Shanxi Province had been such a mess lately.

“The current Military Commissioner is incompetent. You only need to look at the mounted bandits roaming freely the moment the Mount Heng Sword Sect collapsed.”

“If he’s that incompetent, then why not just…”

I swallowed the rest of the sentence before it left my mouth.

*Why should I meddle in someone else’s workplace? Especially when they’re all high-ranking government officials.*

Seeing my reaction, Hong Jin kindly added an explanation.

“The Military Commissioner is appointed directly by the Emperor. His dismissal works the same way.”

“Oh.”

“Well, at least he has no ambitions beyond that. I like bribes too, so I’m hardly in a position to criticize him.”

*What kind of person was this?*

I had seen plenty of politicians on television who claimed to be innocent of all charges of accepting bribes, but Hong Jin was the first person I had met who admitted to liking them so openly.

“Why? Did I look that upright?”

“No. You did look like someone who would enjoy bribes, but…”

“But you didn’t expect me to say it so openly?”

“Something like that. To be honest, I’m a little flustered.”

“Young Master Jin. Do you know what?”

Hong Jin continued with a serious expression.

“I don’t have a thing.”

“What?”

“I’ve been castrated.”

“……”

*What the hell was I supposed to say to that?*

I had suspected as much, but I hadn’t expected him to suddenly drop a bomb like that.

Cheongpung, who had been looking out the window, abruptly joined in with a curious expression.

“What does ‘castrated’ mean?”

“……Please, please shut your mouth.”

*He said he doesn’t have his thing—his thing!*

Every second dragged by. Sweating coldly, I forced myself to speak.

“I’m sorry to hear that.”

“There’s no need to be sorry. Some people live without it, and some people live with it. Right?”

“Th—that’s right.”

His admirable attitude made me solemn for no reason.

Meanwhile, the mountain-dwelling primitive who didn’t know what a eunuch was kept chattering without the slightest sense of danger.

“Benefactor, could you please tell me what a eunuch is?”

*Even if I die, I’m not telling him. Never.*

Even if I explained it, there was a 99.99 percent chance he would say something like, *Wow, I’ve never met anyone without one before!*

But Hong Jin remained composed.

“It means a man doesn’t have his thing.”

“Wow, I’ve never met anyone who didn’t have—”

“Oh, shut up already!”

Cheongpung sucked in a startled breath.

“B-Benefactor.”

“Calm down, Young Master Jin. If he grew up in the mountains, it’s understandable. And besides, it’s not as if I’ve only been living as a eunuch for a day or two.”

“Still, that was too harsh.”

“Was I in the wrong? My sincerest apologies.”

“It’s fine. Chin up. It’s still attached.”

*Decades of experience as a eunuch hadn’t gone anywhere.*

Hong Jin waved his hand as if telling us to calm down, then continued as though nothing important had happened.

“I have never regretted the decision I made. When your own family is starving to death, what wouldn’t you do? Am I wrong?”

“Of course not.”

“I—I would have done the same!”

Whatever Hong Jin said now, we had to agree with him. Cheongpung and I could only nod, feeling like condemned criminals.

“I’m not an upright man, but I’m not cowardly enough to betray my loyalty. If I were, I wouldn’t have continued serving His Highness all this time.”

Hong Jin gazed out the window with hazy eyes.

“I served the late Emperor at his side long ago. He ordered me to assist His Highness Prince Shangshan.”

“The late Emperor?”

If the previous Emperor had entrusted Hong Jin with such a request, it meant he must have held a considerably high position among the palace eunuchs even back then.

Hong Jin nodded and continued.

“I came to the frontier in something like exile, but… I’m satisfied with things as they are now. More than satisfied.”

Despite his words, an unmistakable light shone in his eyes.

Ambition? Hope?

Before I could understand what that light meant, it disappeared, and the coachman’s quiet voice reached my ears.

“We can see the Jin Family of Taiyuan.”
```
