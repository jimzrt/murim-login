<!-- packet-manifest
{
  "included": [
    {
      "path": "source/0120.txt",
      "sha256": "3cec8482765e6bb1d7934a974da40479e262afc9d4ce0cca7c74c0edaaa4098a",
      "bytes": 14133
    },
    {
      "path": "docs/CONTEXT.json",
      "sha256": "b35ac714d82a269a50519dc0787eb7f4ffb0d04e67933dfe7fc5442c10147928",
      "bytes": 4128
    },
    {
      "path": "docs/NAMES.md",
      "sha256": "feb1fc15eee9902d18306b8d166eafaa2fc40d9c9f8b5c03c93b2eda5aeb93aa",
      "bytes": 19029
    },
    {
      "path": "characters/Cheol Mubaek.md",
      "sha256": "e2e26a131b05b7e9654f293cc269de8f556e553e86299a2f8f822baddb639722",
      "bytes": 724
    },
    {
      "path": "characters/Chunsam.md",
      "sha256": "dbf8e1fac54137d93969e25a25328af61c8d9b8ac0b7b0276ecd3e1d87ca414d",
      "bytes": 559
    },
    {
      "path": "characters/Jin Mukyung.md",
      "sha256": "4a93ab79738ba3d88e887ff4f5a167d55b0cd35aa9fb8b9f7259b5c04817a1a5",
      "bytes": 1326
    },
    {
      "path": "characters/Jin Taekyung.md",
      "sha256": "2b8c9f724019ae06bb26ad33b6f894ed4fbe5f7deb99e4eef340c005f4d24962",
      "bytes": 24117
    },
    {
      "path": "characters/Jopil.md",
      "sha256": "ad652fa5db1d217cdb9c3b859e03f94611093ece87e9faeed20bbba198502c03",
      "bytes": 2804
    },
    {
      "path": "characters/Lee Seowol.md",
      "sha256": "e148257a8cfea555d638f27f7aa4236e026ca88605637697af20ec0301017481",
      "bytes": 917
    },
    {
      "path": "characters/Pung Yang.md",
      "sha256": "13974d265bdda78d8eab1eb3544ce49f348fb1998c1839a82e3f6f94dee0f803",
      "bytes": 1307
    },
    {
      "path": "docs/ADDRESS.md",
      "sha256": "05f382e9d41e20017da3ef8a0906bf0c8e1fdf371061791e6e550bbdbb8d6de0",
      "bytes": 17236
    }
  ],
  "estimated_tokens": 20244
}
-->

# Durable State Update — Chapter 120

Return exactly one JSON object and no Markdown fence. Record only facts established
by this chapter. Do not use tools, edit prose, infer future events, or copy archived
profile continuity.

`context` must contain exactly the durable context schema shown below, with version
1 and safe_through 120. Keep at most
2 continuity_sources. Keep
`active_continuity` to at most 20 concise items, `open_questions` to at most 8
items, and `temporary_decisions` to at most 8 items. Keep the serialized context
under 16384 UTF-8 bytes. Use only chapter
numbers through 120. `profile_updates` may replace one exact, uniquely occurring
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
  "chapter": 120,
  "beat": {
    "plot": ["chapter plot paragraph"],
    "continuity": ["binding continuity item"],
    "translation_decisions": ["binding terminology or voice decision"]
  },
  "context": {
    "version": 1,
    "safe_through": 120,
    "continuity_sources": [120],
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
    "Cheol Mubaek was critically injured after Pung Yang defeated him using a Temporary Strength Pill.",
    "Pung Yang possesses the Crimson Blood martial arts and has reached the Peak realm through them and the Temporary Strength Pill.",
    "Pung Yang can temporarily manifest imperfect Sword Force and can maintain powerful Body-Protecting Qi after taking the pill.",
    "Pung Yang has reached approximately seventy percent mastery of the Crimson Blood Twelve Sabers.",
    "Jin Mukyung is a young Peak-level swordsman known as the Heaven Shaking Sword.",
    "Jin Taekyung is a First Rate martial artist who uses One Annihilation with his iron spear.",
    "Jin Mukyung's visible duel with Pung Yang ended in Mukyung's favor, but Pung Yang's concealed throwing knives left Mukyung unconscious.",
    "Pung Yang killed more than ten Mount Heng Sword Sect martial artists after incapacitating Mukyung.",
    "Pung Yang plans to take both Jin brothers and obtain the Jin Family of Taiyuan's martial arts formulas.",
    "Jin Taekyung has taken the Blazing Flame Divine Pill, temporarily gaining Scorching Yang Qi and raising his internal energy from fifteen to forty-five years.",
    "The Blazing Flame Divine Pill's energy may kill Taekyung if he cannot control it, and the System has created the Divine Pill Absorption Quest.",
    "The pill's temporary energy increase lets Taekyung read and evade Pung Yang's attacks more effectively.",
    "Pung Yang knows the Temporary Strength Pill is a secret legacy of demonic, heterodox arts and has taken it several times.",
    "Pung Yang cut Taekyung's iron spear to less than half its length, but Taekyung learned his attack pattern.",
    "Taekyung's dagger inflicted a serious internal injury on Pung Yang by striking before his Body-Protecting Qi fully formed.",
    "Taekyung's thirty years of Scorching Yang Qi is running wild and has caused severe internal injury and a major drop in all stats.",
    "Pung Yang's Temporary Strength Pill began losing its effect after approximately half a shichen; he will not use his last pill because taking three consecutively could endanger his life.",
    "Lee Seowol and nine other surviving Mount Heng Sword Sect martial artists made a last stand to buy Taekyung time to escape with Jin Mukyung and asked him to avenge them.",
    "Taekyung's One Annihilation was defeated, after which Pung Yang severely injured and seized him.",
    "The Unnamed Sword's Ten-Thousand-Year Cold Iron destroyed Pung Yang's Body-Protecting Qi at the chapter's endpoint; neither man's final fate is established."
  ],
  "continuity_sources": [
    119
  ],
  "open_questions": [
    "Can Taekyung survive his severe injuries and the runaway Scorching Yang Qi?",
    "Can Taekyung defeat Pung Yang now that the Unnamed Sword has destroyed his Body-Protecting Qi?",
    "Can Pung Yang survive his internal injury and the loss of his Body-Protecting Qi?",
    "Will Lee Seowol and the nine other surviving Mount Heng martial artists survive their last stand?",
    "Will Jin Mukyung recover from the five concealed throwing knives?",
    "Will Pung Yang obtain the Jin Family's martial arts formulas?",
    "What is the origin and full long-term effect of the Temporary Strength Pill?",
    "What lasting consequences will the Blazing Flame Divine Pill have if Taekyung survives?"
  ],
  "safe_through": 119,
  "temporary_decisions": [
    "Render 일류 초입 and 절정 초입 as early First Rate and early Peak.",
    "Render 잠력단 as Temporary Strength Pill and 호신강기 as Body-Protecting Qi.",
    "Render 격산타우 as Striking the Ox Across the Mountain and 북망산 as Mount Beimang, with a burial-ground footnote.",
    "Render 열화신단 as Blazing Flame Divine Pill and 반 갑자 as half a jiazi, clarified as thirty years.",
    "Retain Narye tagon for 나려타곤 with a footnote explaining the idiom.",
    "Render 만년한철 as Ten-Thousand-Year Cold Iron.",
    "Render 이름 없는 검 as Unnamed Sword.",
    "Render one 식경 as one meal's time in this passage."
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

## Exact glossary matches

| 무림     | **Murim**          |
| 진태경    | **Jin Taekyung**   |
| 진무경    | **Jin Mukyung**    |
| 이소월    | **Lee Seowol**     |
| 철무백    | **Cheol Mubaek**   |
| 조필     | **Jopil**          |
| 항산호    | **Tiger of Mount Heng**       | Cheol Mubaek   |
| 태원진가   | **Jin Family of Taiyuan**        |
| 항산검문   | **Mount Heng Sword Sect**        |
| 절정     | **Peak**          |
| 무인     | **martial artist**                               | Default term                                          |
| 고수     | **master**                                       | Strong/skilled martial artist                         |
| 공력     | **internal energy**                              | Years of 공력 → years of internal energy                |
| 열양지기   | **Scorching Yang Qi**                            | Fire-aligned qi                                       |
| 살기     | **killing intent**                               |                                                       |
| 검기     | **Sword Energy**                                 | When functioning as projected weapon qi               |
| 운기조식   | **circulate one's qi**                           | Usually better as a verb than a proper-name technique |
| 가주     | **Family Head**                              |
| 소가주    | **Lesser Family Head**                       |
| 문주     | **Sect Leader**                              |
| 시스템              | **System**                     |
| 상태               | **Status**                     |
| 레벨               | **Level**                      |
| 경험치              | **EXP**                        |
| 명성               | **Fame**                       |
| 퀘스트              | **Quest**                      |
| 보상               | **Reward**                     |
| 산서     | **Shanxi**             |
| 태원     | **Taiyuan**            |
| 항산     | **Mount Heng**         |
| 본문      | **our sect / this sect**                                        |
| 귀가      | **your family**                                                 |
| 춘삼 | **Chunsam** | Lower District Sect martial artist serving as the carriage driver. |
| 풍양 | **Pung Yang** | Personal name of the Red Wind Band Leader. |
| 소월 | **Seowol** | Short form of Lee Seowol used by Cheol Mubaek. |
| 문주님 | **Sect Leader** | Honorific title Lee Seowol orders the senior figures to use. |
| 잠력단 | **Temporary Strength Pill** | Rare pill that temporarily enhances strength; Pung Yang has only three and uses one against Cheol Mubaek and another during the battle. |
| 호신강기 | **Body-Protecting Qi** | Powerful defensive qi barrier that shields Pung Yang. |
| 열화신단 | **Blazing Flame Divine Pill** | Dangerous elixir that grants half a jiazi of internal energy while risking death from its fire qi. |
| 내상 | **Internal Injury** | System condition label for internal injury. |
| 만년한철 | **Ten-Thousand-Year Cold Iron** | Material that destroys Pung Yang's Body-Protecting Qi when the Unnamed Sword satisfies a specific condition. |

## Listed compact profiles

### Cheol Mubaek.md

# Cheol Mubaek (철무백)

- **Safe through:** Chapter 119
- **Aliases:** Tiger of Mount Heng
- **Role:** Peak master known as the Tiger of Mount Heng; longtime close friend and peer of Lee Cheonbaek; protector of Lee Seowol
- **Personality:** Fierce, short-tempered, intimidating, and fiercely protective; becomes gentle and attentive toward Seowol
- **Voice:** Roaring and confrontational when rebuking the Mount Heng senior figures; gentle and affectionate when speaking to Seowol
- **Relationships:** Close friend and peer of Lee Cheonbaek; paternal uncle and protector of Lee Seowol; feared and respected by the Mount Heng Sword Sect's senior figures

### Chunsam.md

# Chunsam (춘삼)

- **Safe through:** Chapter 109
- **Aliases:** None
- **Role:** First Rate Lower District Sect martial artist who posed as the carriage driver for Wolhwa's group
- **Personality:** Silent, disciplined, and lethal; obeys Wolhwa's instructions without hesitation
- **Voice:** Nearly silent; communicates through concise action rather than speech
- **Relationships:** Lower District Sect subordinate serving under Wolhwa; executes a mounted-bandit informant at her direction

### Jin Mukyung.md

# Jin Mukyung (진무경)

- **Safe through:** Chapter 119
- **Aliases:** Heaven Shaking Sword; Jin Family Second Young Master
- **Role:** Second son of the Jin Family of Taiyuan; twenty-three-year-old cadet at Heaven’s Gate Temple; a young Peak-level genius swordsman who won the visible exchange with Pung Yang but was then incapacitated by five concealed throwing knives
- **Personality:** Reserved, terse, and easily irritated by exaggerated praise; glares coldly when Taekyung identifies him
- **Voice:** Quiet and resonant; clipped and blunt in direct speech
- **Relationships:** Taekyung’s older brother and current martial arts instructor; returned to the Jin Family after several years away

### Jin Taekyung.md

# Jin Taekyung (진태경)

- **Safe through:** Chapter 118
- **Aliases:** Sleeping Dragon of Shanxi
- **Role:** Modern-world protagonist; recently fired after seven years at his job; C-rank Hunter who defeated eight B-rank Minotaurs and killed a Level 70 B-rank Minotaur Warrior in one blow; First Rate martial artist standing before the Peak realm; youngest son of the Jin Family of Taiyuan; new owner of a two-story detached house in Goyang intended for his family; Qi Sense reaches a seventy-meter radius
- **Personality:** Hungry, self-aware, dryly observant, and willing to take a questionable opportunity when desperate; treats the impossible as a game until the danger becomes undeniable
- **Voice:** First-person, conversational, dryly self-mocking; uses vivid trap-and-prey imagery, game jargon, and occasional profanity
- **Relationships:** Jin Mukyung’s younger brother and current student; son of a deceased father; supports his mother and younger sibling; has a strained relationship with Lee Seowol, the current Sect Leader of the Mount Heng Sword Sect

### Jopil.md

# Jopil (조필)

- **Safe through:** Chapter 117
- **Aliases:** One Question, One Kill
- **Role:** Wandering martial artist and leader of a special detachment attacking the Jin Family of Taiyuan
- **Personality:** Cruel, amused by violence, and motivated by both payment and the pleasure of hunting his targets
- **Voice:** Smoothly mocking and deceptively gentle when threatening victims
- **Relationships:** Leader of roughly fifty wandering martial artists; commands Black Mountain Blade

### Lee Seowol.md

# Lee Seowol (이소월)

- **Safe through:** Chapter 119
- **Aliases:** None
- **Role:** Current Sect Leader of the Mount Heng Sword Sect; third child of Lee Cheonbaek and his last surviving descendant; publicly insists on being addressed as Sect Leader rather than Young Lady; leads nine other surviving Mount Heng martial artists in a last stand to buy Taekyung time to escape with Jin Mukyung and asks him to avenge them by killing Pung Yang
- **Personality:** Cold, commanding, and composed; capable of stopping a fierce confrontation with a calm request
- **Voice:** Clear and cool, gentle with Cheol Mubaek but frost-cold and firm when asserting her authority
- **Relationships:** Daughter of the deceased Lee Cheonbaek; younger sister of the deceased Young Sect Leader, Lee Seogeun, and Lee Seogwang; Cheol Mubaek's niece and protected charge

### Pung Yang.md

# Pung Yang (풍양)

- **Safe through:** Chapter 119
- **Aliases:** Red Wind Band Leader
- **Role:** Leader of the Red Wind Band, commanding at least two hundred mounted bandits; became a mounted bandit at thirteen, reached First Rate by age thirty, and rose from squad leader to band leader three years ago; discovered the Crimson Blood martial arts and a case containing five Temporary Strength Pills in a hidden plateau tomb, reached the Peak realm in two years, and can temporarily manifest imperfect Sword Force and powerful Body-Protecting Qi by taking a pill; has reached approximately seventy percent mastery of the Crimson Blood Twelve Sabers; after secretly incapacitating Jin Mukyung, resumed killing Mount Heng Sword Sect martial artists; was seriously injured by Taekyung's dagger, defeated One Annihilation, and seized Taekyung, but had his Body-Protecting Qi destroyed by the Unnamed Sword at the chapter's endpoint
- **Personality:** Foxlike, ruthless, observant, controlled, and willing to kill subordinates who disobey his orders
- **Voice:** Calm, concise, and authoritative when issuing orders
- **Relationships:** Leads the Red Wind Band and controls former members of other mounted-bandit groups who joined his force

## Korean source

```text
＃120화



쉭!

느리지만 힘차게 찔러 들어오는 검 한 자루.

짧은 순간, 풍양의 입가에 비웃음이 떠올랐다.

‘그래, 이럴 줄 알았지.’

온갖 암수가 난무하는 고원에서 수십 년을 살았다. 같은 수법에 두 번이나 걸려들 만큼 어리석었다면 진즉 들개 밥이 되었을 것이다.

‘그런데 저 검은 어디서 튀어나온 거지?’

비수도 아니고 저만한 길이의 장검을 어디에 숨겨 놨던 걸까? 풍양은 가벼운 의문과 함께 호신강기를 끌어 올렸다.

스스스스.

예상했던 일이었기에 대처도 빨랐다. 순식간에 솟구쳐 오른 붉은 기가 빈틈없이 몸을 감싼다.

호신강기는 강력한 검기(劍氣)가 아닌 이상 생채기 하나 낼 수 없는 무적의 갑옷. 어린놈의 헛된 발악이 우습기만 했다.

‘지긋지긋한 놈. 이제 그만 죽어라.’

단숨에 진태경의 목을 꺾어 버리려던 그 순간이었다.

푹-!

“……어?”

몸 안을 파고드는 서늘한 냉기, 그리고 그 뒤를 잇는 뜨거운 통증. 풍양은 부릅뜬 눈으로 가슴을 관통한 검을 바라봤다.

‘이게 무슨.’

호신강기가 사라졌다. 아니, 파괴됐다.

진태경의 검은 호신강기를 두부 가르듯 베어 버리고 그의 가슴마저 꿰뚫었다.

피 한 방울 묻지 않은 투명한 검신을 내려다보던 풍양이 신음처럼 내뱉었다.

“만년한철……?”

들어 본 적이 있다. 천하의 그 무엇도 자르고 부술 수 있다는 신병이기(神兵利器)에 관한 이야기를.

“이걸 네놈이 어떻게.”

풍양은 일그러진 얼굴로 검의 주인을 바라봤다. 태원진가의 어린놈은 천진난만하게 눈을 깜빡이더니 입을 열었다.

“와, 이게 되네.”

“이런 개새끼가……!”

당장 목을 꺾어 버리고 싶었지만, 순간 눈앞이 아득해지며 손아귀에서 힘이 풀렸다. 몸 안에 가득 차 있던 힘이 썰물처럼 사라지고 무력감이 차오른다.

‘하필 이럴 때 잠력단의 효력이.’

비틀비틀 물러나는 풍양의 칠공(七空)에서 피가 흘러나왔다.

지금까지 입은 크고 작은 부상과 호신강기가 흩어지며 역류한 공력이 빠르게 그를 죽음으로 몰아가기 시작했다.

‘이대로, 이대로 죽을 수는 없어.’

풍양은 황급히 품을 더듬었다.

아직 잠력단 한 알이 남아 있다. 그것만 먹으면 놈들을 단매에 쳐 죽이고 이 자리를 뜰 수 있다. 잃은 것이 적진 않지만 몸을 추스른 다음 다시 무림에 나오면 되는 거다.

그래, 잠력단을 먹기만 하면…….

툭.

제기랄, 마음이 너무 급했다.

풍양의 다급한 손길에 떨어진 목곽이 땅에 부딪치며 활짝 열렸다. 피처럼 붉은빛이 도는 단환이 또르르 굴러가더니 누군가의 발아래에 멈춘다.

“아, 이게 잠력단이야?”

신기한 듯 잠력단을 주워 살펴보는 진태경을 향해 풍양이 외쳤다.

“내, 내놔라, 어서!”

“여기서 문제, 그런다고 내가 줄까?”

“놈!”

있는 힘을 다해 달려들었지만 이미 망가진 신체는 한계에 달해 있었다. 진태경에게 닿기도 전에 힘이 풀린 다리가 풀썩 주저앉았다.

이제 풍양에게 남은 길은 하나밖에 없었다.

“제발 부탁이다. 내게, 내게 그걸 다오.”

“만약에 준다면?”

풍양이 간절하게 외쳤다.

“다시는 네 눈에 띄지 않으마. 아니, 앞으로 네게 충성을 다하겠다!”

“오, 절정 고수 수하라. 그거 괜찮은데.”

“그, 그렇지? 그러니 어서 내게 잠력단을 다오!”

“일단 내 물건부터 돌려받고.”

“물건?”

그의 의문은 곧 풀렸다. 다가온 진태경이 가슴 한복판에 박혀 있던 검을 쑥 뽑은 것이다.

아찔한 고통과 함께 피가 폭포수처럼 흘렀다.

“쿠에에에엑!”

풍양은 자신이 토해 낸 핏물에 내장 조각이 섞인 것도 눈치채지 못했다.

단지 시야가 점점 어두워지고 소리가 아득히 멀어지는 것을 느꼈을 뿐이다.

그는 죽어 가고 있었고, 간절함에 반쯤 미쳐 있었다.

‘살고 싶다.’

일평생을 무자비한 약탈자로 살아온 풍양이다.

지금껏 무수히 많은 이들의 재물을, 혹은 목숨을 빼앗았지만, 자신이 이런 최후를 맞이할 것이라고는 꿈에도 생각하지 못했다.

“이제, 이제 제발 잠력단을…….”

흐릿한 시선 속, 고개를 가로젓는 진태경의 모습에 그가 애처롭게 중얼거렸다.

“왜? 어째서?”

그러나 대답은 다른 곳에서 들려왔다.

“뭐라? 어째서?”

“저 찢어 죽여도 시원찮을 놈이……!”

살아남은 항산검문의 무인들이 살기 어린 눈빛으로 각자의 병장기를 움켜쥐었다.

이소월 역시 입술을 깨물며 풍양에게로 활을 겨눴지만 진태경이 황급히 만류했다.

“막타 자제 좀…… 아니, 편안하게 죽이기에는 너무 악랄한 놈입니다. 저렇게 천천히 죽어 가도록 두는 게 나아요.”

짧은 시간, 이소월은 결국 수많은 갈등 끝에 활을 내렸다. 그러자 진태경이 풍양에게로 다가가 귓가에 작은 목소리로 속삭였다.

“나도 슬슬 힘들다. 이제 죽자.”

무슨 소리인지는 모르겠지만 하나는 확실하다.

죽음. 풍양은 자신의 죽음이 코앞으로 성큼 다가왔음을 깨달았다.

“원귀가 되어서라도 복수해 주마.”

“아멘. 부디 다음 생에는 비아그라 정도로 만족해라.”

풍양은 헛웃음을 터트렸다. 마지막 순간까지 저놈의 뜻 모를 헛소리를 들어야 하는 자신의 처지가 우습기 짝이 없었다.

‘제기랄. 날씨 하고는.’

고개를 들어 바라본 하늘은 온통 붉었다. 그리고 이내 암흑으로 물들었다.



* * *



스르륵.

풍양의 고개가 꺾임과 동시에 허공에서 축포가 터졌다.

띠링. 띠링. 띠링!



- [Lv.85 풍양]을 처치했습니다!

- [잠력단] 퀘스트를 성공적으로 완료했습니다!

- 막대한 경험치와 명성을 얻었습니다!

- 레벨 업!

- 레벨 업!

.

.



자그마치 다섯 번의 레벨 업과 명성치 상승을 알리던 시스템창은 이윽고 더 반가운 소식을 전해 주었다.



- 퀘스트 성공 보상이 인벤토리에 지급되었습니다!

- 퀘스트 성공 보상으로 [완전 회복]이 즉각 적용됩니다!



‘완전 회복?’

즉각 적용이라더니, 그 말대로 변화는 순식간에 일어났다.

금이 가고 부러졌던 뼈가 붙고, 베이거나 찔린 상처는 씻은 듯이 아물었다. 변화는 외관에서 그치지 않았다.

‘내상이…….’

신체 내부에서도 보이지 않는 회복이 이루어졌다. 모든 내상이 낫는 것까지는 예상했지만 생각한 것 이상의 소득도 있었다.



- [내상]이 모두 회복됩니다!

- 안정된 신체가 새로운 기운을 받아들입니다!

- [열화신단]을 완전히 흡수했습니다!

- [공력]이 45년으로 상승합니다!

- [공력-열양지기]의 특성이 부여됩니다!



열화신단의 완전한 흡수. 그리고 비약적으로 상승한 공력.

사지백해에 가득 찬 힘이 느껴진다. 용암처럼 내 몸을 태우던 열양지기는 어느새 따뜻한 봄바람이 되어 있었다.

‘해냈구나.’

레벨 업을 해서 몸이 어느 정도 회복되면 바로 운기조식으로 열양지기를 다스릴 생각이었는데…… 시스템 덕분에 어려운 일을 손쉽게 해치웠다.

‘세상에, 45년이면 얼마야.’

원래 가지고 있던 것에 비해 세 배, 자그마치 반 갑자(30년)의 공력이 추가로 늘어난 것이다.

‘반 갑자라.’

평범한 상황이었다면 열화신단을 복용하는 것은 뒤로 미뤄졌을 것이다. 그러나 도박처럼 시도했던 일이 신의 한 수가 되어 돌아왔다.

‘천운이 따라 주지 않았다면 죽었겠지만.’

두 번의 천운. 그중 하나는 열화신단이고, 다른 하나는 지금 내 손에 들려 있는 [이름 없는 검]이다.

모두 몇 달 전 조필을 쓰러트리고 얻은 전리품들.

‘이게 아니었으면 정말 큰일 날 뻔했어.’

그저 다른 검들보다 조금 더 날카롭고 단단한 검이라고 생각했는데, 이게 사실은 만년한철이고, 그런 효능이 있는 줄은 꿈에도 몰랐다.

그런 의미에서 오늘의 내게는 운칠기삼(運七技三)이 아니라 운구기일(運九氣一)이라는 말이 더 어울린다.

‘이걸 운이 좋다고 해야 할지는 모르겠지만.’

나는 천천히 주위를 둘러보았다. 거꾸로 꽂힌 병장기의 무덤, 누군가는 한가득 고인 피 웅덩이에 얼굴을 처박은 채로 죽었고 누군가는 부릅뜬 눈으로 여명이 밝아 오는 하늘을 바라보고 있다. 그런 시신들이 무려 수백에 이른다.

“여기 생존자가 있다!”

“춘삼아! 정신 좀 차려 보거라!”

그 참혹한 광경 속에서 부지런히 움직이는 항산검문의 무인들. 몇 안 되는 생존자들을 일사불란하게 구해 내는 그들을 보고 있는데 문득 알 수 없는 위화감에 휩싸였다.

‘뭐지?’

뭔가 중요한 사실 하나를 잊은 것 같은데…….

눈살을 찌푸리던 그때, 죽은 듯이 누워 있던 시체 하나가 상반신을 일으켰다.

“크으으으.”

“아.”

그래, 반갑다 무경아.



* * *



장장 두 시진에 걸친 수색 작업이 끝났을 때쯤, 이소월의 몸은 핏물로 흠뻑 젖어 있었다.

“생존자는?”

“문주님을 포함…… 스물다섯입니다.”

“몇 명이라고?”

“스물다섯 명입니다. 그중 다섯은 오늘을 넘기기 힘들 것 같습니다.”

물어본 이소월도, 대답한 무인도 입을 다물었다.

한때 태원진가와 함께 산서성을 양분하던 항산검문은 이제 더 이상 존재하지 않는다. 남은 것은 부상자들과 약관도 되지 않은 어린 문주뿐이다.

‘이곳을 버리고 도망쳤다면, 처음부터 풍양의 혼인 제안을 받아들였다면 그들을 살릴 수 있었을까?’

후회는 언제나 부질없다. 그러나 이소월은 후회해야 했다.

비록 얼마 남지 않았지만, 그녀는 여전히 일문(一門)의 문주였다. 뼈에 사무치게 고민하고 후회해야 이후에 같은 실수를 하지 않는다.

그것이 오늘 죽은 이들을 위한 속죄고 남은 이들을 위한 노력이다.

‘항산검문은 반드시 살아남는다. 본문을 위해 목숨을 바친 그대들을 위해서라도.’

이소월은 주먹을 움켜쥐었다. 활시위를 당기며 깨진 손톱이 살을 파고들며 피가 배어 나왔지만 고통도 느끼지 못했다.

“다른 사람들은?”

“모두 대전에 있습니다. 태원진가 측에 제법 의술을 아는 여인이 있어 그녀가 부상자들을 돌보는 중입니다만…….”

무인의 낯빛이 어두워졌다. 그만큼 몇몇 부상자들의 상태가 안 좋다는 증거다. 이소월은 더 이상 묻지 않고 대전을 향해 걸음을 옮겼다.

‘추스르기도 전에 또다시 떠나보내는구나.’

참을 수 없는 피로가 전신을 짓눌렀지만 정신력으로 버텼다. 적어도 떠나는 이들의 마지막은 지켜야 하지 않겠는가.

끼이이익.

대전으로 들어서자 태원진가에서 온 이들은 보이지 않았고, 누워 있는 부상자들이 곧장 눈에 띄었다.

항산호 철무백과 십수 명의 무인들이 그녀를 발견하고 말을 건넸다.

“아, 소월이 왔느냐?”

“오셨습니까. 문주님!”

“문주님을 뵙습니다!”

“……?”

기분 탓인가. 어쩐지 죽어 가는 것치고는 다들 활기가 넘친다. 한동안 말없이 그들을 바라보던 이소월은 활기의 정체를 깨달았다.

“회광반조(回光返照)…….”

그제야 저들의 얼굴 위에 짙게 드리운 죽음의 그림자가 보인다. 그녀가 터지려는 울음을 참으며 황급히 돌아선 그 순간이었다.

쿵!

뭔가 단단한 것에 이마를 부딪친 이소월이 비틀거렸다. 쓰러지려는 그녀의 어깨를 크고 단단한 손바닥이 감쌌다.

“아이고, 조심 좀 하시지. 괜찮아요?”

“아, 네.”

“그럼 됐고.”

이소월을 내려다보던 진태경이 피식 웃었다.



* * *



‘회광반조는 무슨.’

새어 나오려는 실소를 간신히 참았다. 철무백과 다른 부상자들은 다들 팔팔하게 살아나는 중이다.

아, 물론 진무경도 마찬가지고.

‘나 아니었으면 어쩔 뻔했나.’

정확히 말하면 퀘스트 보상이 아니었으면 저들 중 절반은 초상을 치렀을지도 모르겠다.

각각 서른 개씩이나 보상으로 지급받은 [뛰어난 금창약]과 [십년하수오]는 외상과 내상 치유에 뛰어난 효과가 있었다.

‘만약을 대비해서 아낄까도 생각해 봤지만…….’

사람이 죽어 가는데 모른 척할 정도로 모진 놈은 아니다. 물론 수량이 많았던 것도 한몫했다.

“안 들어가요?”

“네?”

“안 들어가실 거면 나 먼저 들어가고.”

어쩐지 멍한 채로 선 이소월을 지나치려다가 문득 잊고 있던 게 생각났다. 가만있자, 그걸 어디 뒀더라?

“아, 여기 있다.”

품을 뒤지는 척하면서 인벤토리에서 죽간 하나를 꺼냈다.

“여기요. 우리 형…… 아니, 소가주님이 보내시는 거.”

이소월이 얼떨떨한 얼굴로 죽간을 받아 들기가 무섭게 시스템 알림이 울렸다.

띠링.



- 초대장 전달을 완료했습니다.

- 퀘스트, [어제의 적, 오늘의 동지]를 완수했습니다!



초대장 전달. 두 번 했다가는 사람 잡겠다.
```

## Final English reading copy

```markdown
# Chapter 120

*Shwick!*

A sword thrust forward—slowly, but with tremendous force.

For the briefest moment, a mocking smile appeared at the corner of Pung Yang’s mouth.

*I knew this was coming.*

He had spent decades living on a plateau where every kind of underhanded trick ran rampant. If he had been foolish enough to fall for the same trick twice, he would have become wild-dog food long ago.

*But where did that sword come from?*

It wasn’t a dagger. Where had the brat hidden a longsword that size?

With that slight question in mind, Pung Yang drew up his Body-Protecting Qi.

*Fssssss.*

He had expected this, so his response was quick. Red qi surged upward in an instant and wrapped tightly around his body.

Body-Protecting Qi was invincible armor that nothing short of powerful Sword Energy could put so much as a scratch on. The young brat’s futile struggle was nothing but laughable.

*What an annoying bastard. Just die already.*

He was about to snap Jin Taekyung’s neck in a single motion when—

*Thud!*

“……Huh?”

A chilly coldness pierced into his body, followed by searing pain. Pung Yang stared wide-eyed at the sword that had pierced straight through his chest.

*What the hell?*

His Body-Protecting Qi had vanished.

No—it had been destroyed.

Jin Taekyung’s sword sliced through it as easily as cutting tofu, then pierced Pung Yang’s chest as well.

Pung Yang looked down at the transparent blade, not a drop of blood staining it, and muttered like he was groaning.

“Ten-Thousand-Year Cold Iron……?”

He had heard of it before. Stories about a divine weapon said to be capable of cutting and breaking anything in the world.

“How did you get this?”

Pung Yang glared at the sword’s owner with a twisted expression. The young brat from the Jin Family of Taiyuan blinked innocently before opening his mouth.

“Wow. This actually worked.”

“You fucking bastard……!”

He wanted to snap the brat’s neck right away, but his vision suddenly went hazy, and the strength drained from his fingers. The power that had filled his body vanished like the outgoing tide, leaving only helplessness in its wake.

*The Temporary Strength Pill had to wear off now of all times.*

Blood began flowing from the seven openings in Pung Yang’s face as he staggered backward.

His various injuries, both great and small, combined with the dispersal of his Body-Protecting Qi. The internal energy surging backward through his body began driving him rapidly toward death.

*I can’t die like this. I can’t.*

Pung Yang hurriedly searched inside his robes.

He still had one Temporary Strength Pill left. If he took it, he could beat the bastards to death in a single stroke and leave this place. He had lost quite a lot, but he could recover, then return to the Murim.

Yes. If he just took the Temporary Strength Pill……

*Clatter.*

Damn it. He was too desperate.

The wooden box slipped from Pung Yang’s frantic hand, struck the ground, and sprang open. A pill tinged with a blood-red color rolled across the ground before coming to a stop beneath someone’s foot.

“Oh, is this the Temporary Strength Pill?”

Jin Taekyung picked it up and examined it with curiosity. Pung Yang shouted at him.

“G-Give it to me! Hurry!”

“Here’s a question. Do you think I’ll give it to you just because you ask?”

“You bastard!”

Pung Yang threw himself forward with all his remaining strength, but his ruined body had already reached its limit. Before he could reach Jin Taekyung, his legs gave out and he collapsed.

Only one path remained to Pung Yang now.

“Please. I’m begging you. Give it to me. Give it to me!”

“What if I do?”

Pung Yang cried out desperately.

“You’ll never see me again. No—instead, I’ll swear my loyalty to you from now on!”

“Oh, having a Peak master as a subordinate. That sounds pretty good.”

“R-Really? Then hurry and give me the Temporary Strength Pill!”

“First, I’m taking my property back.”

“Your property?”

His question was answered a moment later. Jin Taekyung approached and yanked the sword from the center of Pung Yang’s chest.

Blood poured out like a waterfall, accompanied by dizzying pain.

“Gueeeeegh!”

Pung Yang did not even notice that chunks of his internal organs were mixed into the blood he vomited.

All he felt was his vision gradually darkening and the sounds around him receding into the distance.

He was dying, and desperation had driven him half-mad.

*I want to live.*

Pung Yang had spent his entire life as a ruthless marauder.

He had stolen the wealth—and sometimes the lives—of countless people, but he had never once imagined that he would meet an end like this.

“Now, now, please give me the Temporary Strength Pill……”

Through his blurred vision, he saw Jin Taekyung shake his head. Pung Yang mumbled piteously.

“Why? Why not?”

But the answer came from somewhere else.

“What? Why?”

“That bastard deserves to be torn limb from limb!”

The surviving martial artists of the Mount Heng Sword Sect gripped their weapons, their eyes brimming with killing intent.

Lee Seowol also bit down on her lip and drew her bow toward Pung Yang, but Jin Taekyung hurriedly stopped her.

“Let’s lay off the finishing blow for now…… No, he’s too vicious to let him die comfortably. It’s better to leave him there and let him die slowly.”

For a brief while, Lee Seowol struggled with herself. In the end, she lowered her bow. Jin Taekyung approached Pung Yang and whispered softly into his ear.

“I’m starting to get tired too. Let’s just die now.”

Pung Yang didn’t know what he meant, but one thing was certain.

Death.

Pung Yang realized that his own death was almost upon him.

“Even as a vengeful ghost, I’ll have my revenge.”

“Amen. In your next life, be satisfied with Viagra.”

Pung Yang gave a hollow laugh. It was absurd that he had to listen to that bastard’s incomprehensible nonsense until the very end.

*Damn. What terrible weather.*

He raised his head and looked at the sky. It was dyed entirely red.

Then it was swallowed by darkness.

* * *

As Pung Yang’s head lolled to the side, celebratory fireworks burst overhead.

*Ding. Ding. Ding!*

> **System**
> - Defeated **Lv. 85 Pung Yang**!
> - Successfully completed the **Temporary Strength Pill** Quest!
> - Obtained a massive amount of **EXP** and **Fame**!
> - Level Up!
> - Level Up!
> - …

After announcing five level-ups and an increase in Fame, the System window delivered even better news.

> **System**
> - The Quest success reward has been delivered to your **Inventory**!
> - **Full Recovery** has taken effect immediately as the Quest success reward!

*Full Recovery?*

It said the effect would be immediate, and the change happened exactly as promised.

Cracked and broken bones knitted back together. Cuts and punctures healed as if they had been washed clean. The changes did not stop at the surface.

*The Internal Injuries……*

Invisible healing took place inside my body as well. I had expected all my Internal Injuries to heal, but there was an even greater benefit than I had imagined.

> **System**
> - All **Internal Injuries** have healed!
> - Your stabilized body accepts new qi!
> - The **Blazing Flame Divine Pill** has been fully absorbed!
> - Your **internal energy** has risen to 45 years!
> - Your **internal energy** has gained the **Scorching Yang Qi** attribute!

The Blazing Flame Divine Pill had been completely absorbed.

And my internal energy had risen explosively.

I could feel power filling every limb and bone. The Scorching Yang Qi that had burned through my body like lava had somehow become a warm spring breeze.

*I did it.*

I had planned to circulate my qi and control the Scorching Yang Qi once my body recovered somewhat from the level-ups, but thanks to the System, I had handled the difficult part with ease.

*Forty-five years? How much is that?*

Compared to what I had originally possessed, it was three times as much—an additional half a jiazi, or thirty years, of internal energy.

*A half jiazi.*

Under normal circumstances, I would have put off taking the Blazing Flame Divine Pill. But the gamble I had taken had come back as a masterstroke.

*I would have died if luck hadn’t been on my side, though.*

Two strokes of heavenly luck.

One was the Blazing Flame Divine Pill, and the other was the **Unnamed Sword** in my hand.

Both were loot I had obtained after defeating Jopil several months ago.

*I would have been in serious trouble without this.*

I had thought it was merely a sword that was a little sharper and harder than other swords. I had never dreamed that it was actually Ten-Thousand-Year Cold Iron, or that it possessed such an ability.

In that sense, the saying *seven parts luck and three parts skill* didn’t suit me today. *Nine parts luck and one part qi* was much more appropriate.[^1]

*Though I’m not sure this can really be called good luck.*

I slowly looked around.

A graveyard of weapons stood with their hilts buried upside down. Some people had died with their faces planted in pools of blood. Others stared wide-eyed at the sky as dawn began to break.

There were hundreds of corpses like that.

“There’s a survivor here!”

“Chunsam! Come around!”

Amid that horrific scene, the martial artists of the Mount Heng Sword Sect moved tirelessly. As I watched them rescue the few survivors with disciplined efficiency, I was suddenly seized by an inexplicable sense of wrongness.

*What is it?*

It felt like I had forgotten something important……

Just as I was frowning, one of the corpses that had been lying motionless raised its upper body.

“Guuuuuh.”

“Oh.”

Right. Good to see you, Mukyung.

* * *

By the time the four-hour search was over, Lee Seowol’s body was soaked in blood.

“How many survivors?”

“Twenty-five, including you, Sect Leader.”

“How many did you say?”

“Twenty-five. Five of them probably won’t make it through today.”

Both Lee Seowol, who had asked the question, and the martial artist who answered it fell silent.

The Mount Heng Sword Sect, which had once divided control of Shanxi with the Jin Family of Taiyuan, no longer existed. All that remained were the injured and a young Sect Leader who was not even twenty years old.

*If I had abandoned this place and fled, if I had accepted Pung Yang’s marriage proposal from the beginning, could I have saved them?*

Regret was always pointless.

But Lee Seowol had to regret.

Although few remained, she was still the Sect Leader of a sect. Only by agonizing over her mistakes and regretting them to the bone could she avoid making the same mistakes again.

That was her atonement to those who had died today and her effort on behalf of those who remained.

*The Mount Heng Sword Sect will survive. If only for those who gave their lives for our sect.*

Lee Seowol clenched her fist. Her fingernails, broken from drawing the bowstring, dug into her flesh as she clenched her fist. Blood seeped out, but she felt no pain.

“What about the others?”

“They’re all in the main hall. There’s a woman from the Jin Family of Taiyuan who knows a fair amount about medicine, and she’s treating the wounded, but……”

The martial artist’s expression darkened. It was proof of just how bad the condition of some of the wounded was.

Lee Seowol did not ask anything else and headed toward the main hall.

*I’m sending them off again before we’ve even had time to recover.*

Unbearable fatigue pressed down on her entire body, but she held on through sheer willpower.

At the very least, she had to see off those who were leaving.

*Creeeeak.*

When Lee Seowol entered the main hall, the people from the Jin Family of Taiyuan were nowhere in sight. The wounded lying on the floor immediately caught her eye.

The Tiger of Mount Heng, Cheol Mubaek, and more than a dozen martial artists noticed her and called out.

“Ah, Seowol. You’ve come?”

“You’re here, Sect Leader!”

“We greet you, Sect Leader!”

“……?”

Was it just her imagination?

For people who were supposedly dying, they seemed strangely full of energy. After silently staring at them for a while, Lee Seowol realized what that energy meant.

“A final rally……”

Only then did she see the dark shadow of death lying heavily across their faces.

Just as she hurriedly turned away to hold back her tears—

*Bang!*

Lee Seowol staggered after striking her forehead against something solid. As she began to fall, a large, firm hand caught her shoulder.

“Oh, careful there. Are you all right?”

“Ah, yes.”

“Then we’re good.”

Jin Taekyung looked down at Lee Seowol and let out a short laugh.

* * *

*Some final rally.*

I barely held back a snort.

Cheol Mubaek and the other wounded were all recovering vigorously.

Of course, Jin Mukyung was no exception.

*What would they have done without me?*

To be precise, if not for the Quest rewards, there might have been funerals for half of them.

The thirty **Superior Wound Medicines** and thirty **Ten-Year He Shouwu** I had received as rewards each had remarkable effects on external and Internal Injury healing.

*I did consider saving them in case of an emergency……*

But I wasn’t heartless enough to ignore people dying right in front of me.

Of course, the sheer quantity had played a part too.

“Aren’t you coming in?”

“What?”

“If you’re not going in, I’ll go in first.”

I was about to walk past Lee Seowol, who was standing there in a daze, when I suddenly remembered something I had forgotten.

*Wait. Where did I put that?*

“Ah, here it is.”

I pretended to rummage around inside my robes and pulled a bamboo slip from my Inventory.

“Here. It’s from my hyung…… no, from the Lesser Family Head.”

Lee Seowol accepted the bamboo slip with a bewildered expression.

The System notification rang the instant she took it.

*Ding.*

> **System**
> - Invitation delivery complete.
> - Quest **Yesterday’s Enemy, Today’s Ally** completed!

Invitation delivery.

If I had to do that twice, someone was going to die.

[^1]: A playful variation on the Korean saying *seven parts luck, three parts skill*, replacing skill with *qi* and shifting the balance even further toward luck.
```
